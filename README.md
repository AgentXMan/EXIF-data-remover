# EXIF-data-remover
This is a tool to remove exifdata from images. It deletes all the extra details stored in the photo such as camera settings (shutter speed, aperture, ISO), date and time the photo was taken, GPS coordinates (if available), camera model, etc related to the image. The mechanism is pretty simple. it just duplicates the image and only puts all the pixel data into the image leaving behind the exifdata.

(this was made for the HackBlue Cyber hackathon: https://hackblue.devpost.com/)
youtube link: https://youtu.be/vYH_PFy0LrA?si=3XqV2-t5ctIZrKnV

# USAGE AND INSTALLATION
=> to use the code. pls install the Pillow module first
=> then in the main() function, simply change the filename(imgToDo) to what your file is. keep in mind the place where the program is located and your file should be in the same directory.


