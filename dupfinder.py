#!/usr/bin/python

from optparse import OptionParser
import os
import hashlib
import shutil

class comparison_data:
    def __init__(self, md5_digest="", filename="", full_filenames="", count=0):
        self.md5_digest = md5_digest   # this the md5sum
        self.filename = filename;
        if full_filenames == None:
            self.full_filenames = []      # this is a list of filenames
        else:
            self.full_filenames = [full_filenames]
        self.count = count           # thsi is the number files that contains the same md5sum

# list that contains the majority of data.
datalist = []    

parser = OptionParser()
parser.add_option( "-x", "--ext", dest="file_extension", help="the extension used for file filter")
parser.add_option( "-p", "--path", dest="path", help="file path to use")
parser.add_option( "-d", "--dst", dest="destination", help="where the unique files are to be copied into")
parser.add_option( "-l", "--limits", dest="max_number_of_files", help="set a limit on the number of files to process")

(options, args)=parser.parse_args()

# check if there is a limit to the number of files to parse.
if (options.max_number_of_files != None):
    max_number_of_files = options.max_number_of_files
else:
    # set the number of files to unlimited
    max_number_of_files = -1
    
# check on a file extension, or it defaults to *.jpg
if (options.file_extension != None):
    filter_file_extension = options.file_extension
else:
    filter_file_extension = ".jpg"
    
# check if there is a file path specified
if (options.path != None):
    file_path = options.path
else:
    file_path = "./"
    
# check if the there is a destination for the files
if (options.destination != None):
    file_destination = options.destination
else:
    file_destination = "./Copied"
    
for dirname, dirnames, filenames in os.walk(file_path):

    # search through each file it encountered.
    for filename in filenames:
        file_basename, file_extension = os.path.splitext(filename)
        
        if (file_extension == filter_file_extension)  : 
            datafile = os.path.join(dirname, filename)
            
            # Open,close, read file and calculate MD5 on its contents 
            with open(datafile) as file_to_check:
                
                # read contents of the file
                data = file_to_check.read()    
                # pipe contents of the file through
                md5_returned = hashlib.md5(data).hexdigest()
    
                # check through the list to see if there is any items in there
                # the same md5.            
                data_found = False
                for i in range(0,len(datalist)):
                    if (md5_returned == datalist[i].md5_digest):
                        datalist[i].count += 1
                        datalist[i].full_filenames.append(datafile)
                        data_found = True
                
                # data was not found so we append it to the file.        
                if (data_found == False):        
                    x = comparison_data(md5_returned, filename, datafile, 1);
                    datalist.append(x);
                    
    # print out some progress report
    print dirname + "  number of files = " + str(len(datalist))            
            
print "found " + str(len(datalist)) + " number of unique files"
for i in range(0,len(datalist)):
    print "Copying " + datalist[i].full_filenames[0] + " --> " + file_destination + "/" + datalist[i].filename
    shutil.copy(datalist[i].full_filenames[0], file_destination + "/" + datalist[i].filename)
#    print datalist[i].count
#    print datalist[i].filenames
#    print datalist[i].md5_digest
            
