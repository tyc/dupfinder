dupfinder
=========

duplicate finder for files.

This python script will search through a specified directory for all the files and 
copy one instance of them into another directory. It leaves the original files and
directories untouched.

A new directory called Copied is created at working directory where these files
are copied into.

running dupfinder.py
====================
Usage: dupfinder.py [options]

Options:
  -h, --help            show this help message and exit
  -x FILE_EXTENSION, --ext=FILE_EXTENSION
                        the extension used for file filter
  -p PATH, --path=PATH  file path to use
  -d DESTINATION, --dst=DESTINATION
                        where the unique files are to be copied into
  -l MAX_NUMBER_OF_FILES, --limits=MAX_NUMBER_OF_FILES
                        set a limit on the number of files to process


The problem it is trying to solve.
==================================

My wife and I take a lot of photos with our phones. When I transfer them onto our 
computer, there is no way of knowing whether I have already transferred the files 
to the computer or not. So to be safe, I copied all the files from the phone to
the computer, and clean up the files on the computer.

The reason for doing this
=========================

There are quite a few duplicate finders available, but as an exercise for me to learn
python, I have undertaken this project.

The algorithm
=============
For the specified path, the python script will search for a file that matches the
specified file extension. When it finds it, it will generate a md5 digest for that
file. With the generated md5 digest, it searches through its already logged file if
there is already a file with the same md5 digest. If it has, it will increase the
count for that md5 digest. For that digest, it will also logged the full path. When
all the files have been filtered, it will interate over each in the list and copied
it to the destination folder.

