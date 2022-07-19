import os
import shutil
from pathlib import Path

def sort_files():

    downloadspath = str(os.path.join(Path.home(), "Downloads"))
    print("Sorting files in directory: " + downloadspath)

    files = os.listdir(downloadspath)

    #Defining destination folder paths
    try:
        pdf = str(os.path.join(downloadspath, "pdf_downloads"))
        image = str(os.path.join(downloadspath, "image_downloads"))
        docx = str(os.path.join(downloadspath, "docx_downloads"))
        xlsx = str(os.path.join(downloadspath, "xlsx_downloads"))
        zip = str(os.path.join(downloadspath, "zip_downloads"))
        dmg = str(os.path.join(downloadspath, "dmg_downloads"))
        pptx = str(os.path.join(downloadspath, "pptx_downloads"))
        other = str(os.path.join(downloadspath, "other_downloads"))
    except:
        print("Sorting directories does not exist. You need the following directories in your Downloads-folder: ")
        print("pdf_downloads")
        print("image_downloads")
        print("docx_downloads")
        print("xlsx_downloads")
        print("zip_downloads")
        print("dmg_downloads")
        print("pptx_downloads")
        print("other_downloads")

    files_sorted = 0

    for file in files:
        if file.endswith(".pdf") or file.endswith(".PDF"):
            shutil.move(os.path.join(downloadspath, file), pdf)
            files_sorted += 1

        if file.endswith(".docx"):
            shutil.move(os.path.join(downloadspath, file), docx)
            files_sorted += 1

        if file.endswith(".xlsx"):
            shutil.move(os.path.join(downloadspath, file), xlsx)
            files_sorted += 1

        if file.endswith(".zip"):
            shutil.move(os.path.join(downloadspath, file), zip)
            files_sorted += 1

        if file.endswith(".dmg"):
            shutil.move(os.path.join(downloadspath, file), dmg)
            files_sorted += 1

        if file.endswith(".pptx"):
            shutil.move(os.path.join(downloadspath, file), pptx)
            files_sorted += 1

        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".HEIC") or file.endswith(".svg"):
            shutil.move(os.path.join(downloadspath, file), image)
            files_sorted += 1
    """
        if (file[0] != '.') and ('.' in file):
            shutil.move(os.path.join(downloadspath, file), other)
            files_sorted += 1
    """
    
    print("Completed! " + str(files_sorted) + " files sorted.")
    
def main():
    sort_files()

if __name__ == "__main__":
    main()