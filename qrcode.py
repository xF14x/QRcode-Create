import pyqrcode as qqrr # Programming By Suliman Almohawis | Twitter {F14Commander} GitHub {xF14x}
print("")
text = input("Please Enter your Massage OR Link : ")
FileName = input("Please Enter File Name : ")
# to create the qrcode :
g = qqrr.create(text)
# to save the qrcode image :
g.png(FileName + ".png",scale=10)
print("")
print("Created By Suliman Almohawis | Twitter {F14Commander}")
print("")
