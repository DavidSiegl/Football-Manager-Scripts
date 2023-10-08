import os
import argparse

folder_path = input("Folder: ")
files_array = []

for file in os.listdir(folder_path):
    if file != "config.xml":
        files_array.append(file.replace(".png", ""))
    
with open("./config_template.xml", "r") as f:
    lines = f.readlines()
    f.close()
            
lines_count = len(lines)
for player_id in files_array:
    lines.insert(lines_count - 2, "\t\t<record from=\"" + player_id + "\" to=\"graphics/pictures/person/" + player_id + "/portrait\"/>\n")
                    
with open(folder_path + "/config.xml", "w") as f:
    f.writelines(lines)
    f.close()      