
# Scope : Remove duplicate entry of songs in specified folder which may contain differnt sub folders
# If artist, album,size remains same delete the duplicates
# If artist ,album remains same. But not size , Delete the file which sizes low .
# File name format:  Song start _ Artist _Album

import os
import mp3_tagger
from mp3_tagger import MP3File
Fol_Search=r'D:\Main'
file_address={}
#*********************************
pass_condition=True
while pass_condition:
    for r1,fol_1,fil_1 in os.walk(Fol_Search):
        all_root_files=[file for file in fil_1]
        for file in all_root_files:
            if file.endswith('.mp3'):

                filepath=r1+r'/'+file
                song=MP3File(filepath)

                Name=song.artist
                song.set_version(mp3_tagger.id3.VERSION_2)
                if type(Name)==type(''):
                    Art_name=Name.split('-')[0].strip()
                    song.artist=Art_name

                song.save()
                all=song.get_tags()
                size_bytes=os.path.getsize(filepath)
                #size_mb=size_bytes/(1024*1024)
                print(all)
                file_address[filepath]=[song.artist,size_bytes]

        if len(fol_1)>=1:
            for each_folder in fol_1:
                pass_condition=True
                Fol_Search=r1+r'/'+each_folder
        else:pass_condition=False

print(file_address)
