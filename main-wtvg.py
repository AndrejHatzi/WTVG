import os;
import wikipedia;
import time;
from gtts import gTTS;
import moviepy.editor as mp;
from mutagen.mp3 import MP3;
from image_download import get_images;
from typing import List;

topic : List[str] = ["The Witcher (TV series)",
"Donald Trump",
"Underground (film)",
"Deaths in 2019",
"List of Star Wars films",
"National Register of Citizens of India",
"Cats (2019 film)",
"Impeachment inquiry against Donald Trump",
"List of presidential impeachments",
"Billie Eilish",
"Scarlett Johansson",
"Jimmy Hoffa",
"Crisis on Infinite Earths (Arrowverse)",
"Richard Jewell",
"Mikel Arteta",
"Star Wars",
"Jumanji The Next Level",
"UFC 245"];
def text_to_audio(language:str, topic:str)->None:
	#page = wikipedia.page("google");
	mytext = wikipedia.summary(topic);
	myobj = gTTS(text=mytext, lang=language, slow=False);
	myobj.save("current.mp3");

def image_to_video(topic:str)->None:
	os.system("ffmpeg -f image2 -r 1/5 -i imgs/{}/%0d.jpg -vcodec mpeg4 -y current.mp4".format(topic.replace(' ','_')));

def merge_AudioVideo(topic:str):
	audio = MP3("current.mp3");
	video = mp.VideoFileClip("current.mp4").subclip(0,audio.info.length);
	video.write_videofile("{}.mp4".format(topic), audio="current.mp3");

def deleteFiles(topic:str):
	try:
		os.remove("current.mp4");
		os.remove("current.mp3");
	except:
		pass
	#os.rmdir("imgs/{}/".format(topic.replace(' ','_')));


def main():
	i : int;
	for i in range(len(topic)):
		try:
			print("Mined {} of {}".format(i, len(topic)));
			theme:str = topic[i];
			text_to_audio("en", theme);
			time.sleep(15);
			get_images(False, theme, 100, "imgs/");
			image_to_video(theme);
			merge_AudioVideo(theme);
			deleteFiles(topic);
		except:
			print("System Halted on: {}".format(i))

def GenerateVideo(theme:str, language:str):
	text_to_audio(language, theme);
	time.sleep(15);
	get_images(False, theme, 100, "imgs/");
	image_to_video(theme);
	merge_AudioVideo(theme);

#GenerateVideo("Meme", "en-ie");


main();
#deleteFiles("The Mandalorian");


#text_to_audio("en", "The Mandalorian");