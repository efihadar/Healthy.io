import datetime
import os

for root, dirs, files in os.walk("e"):
    for filename in files:
        filename1 = filename.replace(".gz", "")
        date_time_str = filename1
        date_time_obj = datetime.datetime.strptime(date_time_str, '%d-%m-%y')
        now = datetime.datetime.now()
        current_time = now.strftime("%H-%M-%S")

        print("Old file name: " + root + "\\" + filename)
        print("New file name: " + root + "\\" + str(date_time_obj.date()) + "T" + current_time + ".gz")

        ##Actual name change
        #os.system("mv " + root + "\\" + filename + root + "\\" + str(date_time_obj.date()) + "T" + current_time)

    aws s3 --recursive mv s3://efibackups/<folder_name_from> s3://efibackups/<folder_name_to>
