# Turn video to audio
# find *.mp4 uner '/Users/noureddinbakir/PycharmProjects/AI-Shorts-Creator/finished' that don't have "_full" in their name and turn them to audio
import os
import subprocess
# get all files in the directory
# there are directories that include the audio files, so recursively go through all directories and get all files
import subprocess

def main():
    for root, dirs, files in os.walk("/Users/noureddinbakir/PycharmProjects/AI-Shorts-Creator/finished"):
        for file in files:
            if file.endswith(".mp4") and "_full" not in file:
                path = os.path.join(root, file)
                name = file.split(".")[0]

                # turn the video to audio
                subprocess.run(["ffmpeg", "-i", path, "-ab", "160k", "-ac", "2", "-ar", "44100", "-vn", path.split(".")[0] + ".wav"])

                # move the audio file to the audio subdirectory
                subprocess.run(["mv", path.split(".")[0] + ".wav", f"/Users/noureddinbakir/PycharmProjects/AI-Shorts-Creator/finished/audio/{name}.wav"])

if __name__ == "__main__":
    main()