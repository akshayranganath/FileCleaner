# File Cleaner

This is a simple utility file to help with removing needless Nikon Raw (NEF) images.

## Description
When using Nikon for taking pictures, if you are shooting in a combined mode, you will end up with 2 sets of images:

- *.JPG: JPEG files
- *.NEF: Nikon format of the raw images

If you are like me, you'll view the JPG images and start deleting them from whatever tool you are using. This will leave behind a trail of un-needed NEF files.

The purpose of this script to pick up such orphaned raw images and delete them.

## Usage

The code requires python. Here's the message on usage from the command's help option.

```bash
$ python file_cleaner.py --help
usage: file_cleaner.py [-h] --folder FOLDER [--test] [-v]

Directory cleaner: It finds deleted JPG files and deletes the corresponding
.NEF file in the sub-folder named "raw"

optional arguments:
  -h, --help       show this help message and exit
  --folder FOLDER  Folder to check for .JPG files
  --test           Just print the names of file that will be deleted.
  -v, --verbose    Bump up the logging level to see names of each file being
                   deleted.
```

## Feedback
If you have any feedback, please leave me a note.
