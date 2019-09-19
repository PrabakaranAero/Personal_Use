#******************************************************************************************************
# Scope : Remove duplicate entry of songs in specified folder which may contain differnt sub folders
# If artist, album,size remains same delete the duplicates
# If artist ,album remains same. But not size , Delete the file which sizes low .
# File name format:  Song start _ Album Name_Artist

# There must be some entry in Title , Album, artists

# version 0.0
# Date : 17 June 2019

# Version 0.0 works only for songs in a folder , it doesnot care about sub folder and finding duplicates

#******************************************************************************************************

import os
import mp3_tagger
from mp3_tagger import MP3File
Fol_Search=r'C:\Users\Prabakaran\Desktop\Trail_mp3\Selections_tamil'
from pprint import pprint

FileWithAddress={}
To_remove=['NewTamilHitsCom','VmusiQ.Com','SenSongsMp3.Co','StarMusiQ.Com','MassTamilan.com',
           'StarmusiQ.io','AudioTamil.NET','Masstamilan.In','isaimini.co','TamilWire.com',"TamilTunes.com",
           'Masstamilan.in']
#*********************************
pass_condition=True

#******************************************************************************************************
def Unwanted_Details_Remove(item):   # Item should be string song title,artist or album
    item_name=''
    final_item_name=''
    try:
        l1=len(item)
        for rm_item in To_remove:
            item_name = item.replace(rm_item,'')
            if l1!=len(item_name):break

    except AttributeError:
        pass
    final_item_name = ''.join([e for e in item_name if e.isspace() or e.isalnum() or e==','])
    return final_item_name

#*********************************************************************************************************

while pass_condition:
    for r1,fol_1,fil_1 in os.walk(Fol_Search):
        all_root_files=[file for file in fil_1]
        for file in all_root_files:
            if file.endswith('.mp3'):
                filepath=r1+r'/'+file
                song=MP3File(filepath)
                song.set_version(mp3_tagger.id3.VERSION_2)
                pr_name_song=(song.song)
                if song.song:song_name=Unwanted_Details_Remove(pr_name_song)
                if song.artist:artist_name=Unwanted_Details_Remove(song.artist)
                if song.album:album_name=Unwanted_Details_Remove(song.album)
                new_file_name=song_name+'_'+album_name+'_'+artist_name+'.mp3'
                song.artist=artist_name
                song.album=album_name
                song.song=song_name

                song.save()
                #all=song.get_tags()
                size_bytes=os.path.getsize(filepath)
                FileWithAddress[filepath]=[song.artist,size_bytes,song_name]
                try: os.rename(filepath,r1+r'/'+new_file_name)
                except FileExistsError:pass
        if len(fol_1)>=1:
            for each_folder in fol_1:
                pass_condition=True
                Fol_Search=r1+r'/'+each_folder
        else:pass_condition=False


#print(FileWithAddress)



