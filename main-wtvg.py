import os;
import wikipedia;
from gtts import gTTS;
import moviepy.editor as mp;
from mutagen.mp3 import MP3;
from image_download import get_images;
from typing import List;


def text_to_audio(language:str, topic:str)->None:
	#page = wikipedia.page("google");
	mytext = wikipedia.summary(topic);
	myobj = gTTS(text=mytext, lang=language, slow=False);
	myobj.save("current.mp3");

def image_to_video(topic:str)->None:
	os.system("ffmpeg -f image2 -r 1/5 -i imgs/{}/%0d.jpg -vcodec mpeg4 -y current.mp4".format(topic.replace(' ','')));

def merge_AudioVideo(topic:str):
	audio = MP3("current.mp3");
	video = mp.VideoFileClip("current.mp4").subclip(0,audio.info.length);
	video.write_videofile("{}.mp4".format(topic), audio="current.mp3");

def deleteFiles(topic:str):
	os.remove("current.mp4");
	os.remove("current.mp3");
	os.rmdir("imgs/{}".format(topic.replace(' ','')));


def main():
	topic:str = "The Mandalorian";
	text_to_audio("en", topic);
	get_images(True, topic.replace(' ',''), 100, "imgs/");
	image_to_video(topic);
	merge_AudioVideo(topic);



main();


#text_to_audio("en", "The Mandalorian");