'''
made by AgentXMan
(BasicCode on YT, link given below)

simple logic

1. open file
2. empty metadata 
(duplicating the image so that only the pixel data is saved and not the exif data)
3. save as new file


this makes it so the additional metadata (like location or gps coordinates) are removed
from the file. 

This is for HackBlue Cybersec hackathon 
(https://hackblue.org/competitions/hackathon.html)
(https://hackblue.devpost.com/)

youtube video link: 
https://youtu.be/vYH_PFy0LrA?si=VXKnLQxNB0Q7FmCS
'''

from PIL import Image

def openFile(filepath):
    img = Image.open(filepath)
    return img

def deleteMetaData(imgg):
    data = list(imgg.getdata())
    image2 = Image.new(imgg.mode, imgg.size)
    image2.putdata(data)
    image2.save('withoutExif.jpeg')
        
    print("image without exif saved")
    return image2
    
def main():
    imgToDo = openFile("filename.jpg")
    deleteMetaData(imgToDo)


if __name__ == "__main__":
    main()
