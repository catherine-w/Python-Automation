import os, time
from datetime import date

#renaming videos in folder
def main():

    path = os.chdir("C:\\Users\\cathe\\Pictures\\videos 2020")

    for video in os.listdir(path):

        new_video_name = time.ctime(os.path.getctime(video))
        new_name = (new_video_name.replace(":", "-") + ".MOV")
        print (new_name)
        os.rename(video, new_name)

#Driver code
if __name__ == '__main__':
    main()
