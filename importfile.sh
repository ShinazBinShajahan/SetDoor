echo "enter the path of php file"
read name
aa=`find //sdcard/ -name $name`
if [ $aa ]
then
cp $aa $HOME/SetDoor
echo "succes"
else
echo "not found"
fi