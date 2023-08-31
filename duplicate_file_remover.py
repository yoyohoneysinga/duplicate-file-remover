import os

folder1 = "location1"
folder2 = "location2"

files1 = os.listdir(folder1)
files2 = os.listdir(folder2)

for file in files1:

    if file in files2:

        os.remove(os.path.join(folder1, file))
        print(f"Deleted {file} from {folder1}")

print("Finished comparing and deleting files.")
