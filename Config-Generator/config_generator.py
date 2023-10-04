import os
import argparse

folder_path = input("Folder: ")
files_array = []

for file in os.listdir(folder_path):
    files_array.append(file) 
    if file == "config.xml":
        with open(folder_path + "/config.xml", "r+") as f:
            for player_id in files_array:
                lines = f.readlines()
                lines_count = len(lines)
                lines.insert(lines_count - 2, "\t<record from='" + player_id + "to='graphics/pictures/person/" + player_id + "/portrait'/>\n".expandtabs(2))
            f.truncate()
            f.writelines(lines)
            f.close()
    #else:
        