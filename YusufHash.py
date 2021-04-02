# Name: Yusuf Ahmad Azani
# Section: Section 4341
# Assignment: Lab08

import os
import sys
import hashlib
import datetime

indicator = 0

def main():

    for files in os.walk("/var/www/html/lab08", topdown=False):

        #initialHash()

        # Refer email details for question 1.
        # Detecting if the csv file already exists, then only a 
        # hash and compare function would be required.
        if "lab08.csv" in files:
            print("yay")
            hashCompare()
        
        # If a csv file was not detected in the directory, then
        # run the initial hashing function with write.
        else:
            initialHashwithWrite()
        
# Refer email details for question 2.
def hashCompare():

    # Creating a dictionary with each scenario with the filepath 
    # as the key and the hashed output as the value.

    # The dictionary below is for key-value pairs taken from the 
    # most current run of the hash function.
    dictCurrent = {} 
    
    # The dictionary below is for key-value pairs taken from the 
    # csv file that was originally created.
    dictCSV = {}

    # The dictionary below is for key-value pairs indicating a 
    # modified line in the csv file where the pathname matches
    # but the hash value does not.
    dictMod = {}

    # The dictionary below is for key-value pairs indicating a 
    # new entry where the pair is present in the current run
    # but not in the original CSV file.
    dictNew = {}

    # The dictionary below is for key-value pairs indicating a 
    # removed entry where the pair is not present in the current
    # run but is present in the original CSV file.
    dictRMV = {}

    #------------------Hash function Start-----------------------

    for root, dirs, files in os.walk("/", topdown=False):
        
        if "/usr" in root:
            indicator = 1

        elif "/boot" in root:
            indicator = 1

        elif "/bin" in root:
            indicator = 1
        
        elif "/etc" in root:
            indicator = 1

        elif "/dev" in root:
            indicator = 1

        elif "/proc" in root:
            indicator = 1
        
        elif "/run" in root:
            indicator = 1

        elif "/sys" in root:
            indicator = 1

        elif "/tmp" in root:
            indicator = 1
        
        elif "/var/lib" in root:
            indicator = 1

        elif "/var/run" in root:
            indicator = 1

        elif "/var/ossec/queue" in root:
            indicator = 1

    
        else:
            indicator = 0
            for name in files:
                
                path = os.path.join(root, name)
                fd = open(path, "rb")
                fdread = fd.read()
                hashed = hashlib.sha256(fdread).hexdigest()

    #------------------Hash function End-----------------------

                # Assigning the pathnames and hashed values from the
                # most recent run to the "dictCurrent" dictionary as
                # key-value pairs.
                dictCurrent[path] = hashed

    # Opening the original csv file in read to avoid modifying the file.
    initial = open("lab08.csv", "r")

    # A for loop to iterate through each line in the CSV file.
    for line in initial:

        # Splitting each line at the "," where index 0 will be the path
        # and index 1 will be the hashed output.
        work = line.split(",")

        # Assigning the pathnames and hashed values from the original
        # CSV file to the "dictCSV" dictionary as the key-value pairs.
        dictCSV[work[0]] = work[1]

    #---------------------Comparing Process Start-------------------

    # For loop to iterate through each key (path) in the current 
    # dictionary.
    for pathCurrent in dictCurrent:

        # Testing to see if a key that is present in the current
        # dictionary is also present in the original CSV dictionary.
        if pathCurrent in dictCSV:
            
            # Comparing the hashed values of the same key (filepath).
            if dictCurrent.get(pathCurrent) != dictCSV.get(pathCurrent):

                # If the same key is present in both files but the hash
                # values differ, this indicates a modified file which is
                # then placed into the modified dictionary that I will
                # use later in the program.
                dictMod[pathCurrent] = dictCurrent.get(pathCurrent)

                # TESTING LINE ONLY
                print("Found something modified!", pathCurrent)

        # If a key-pair value is in the current dictionary but no in
        # the original CSV dictionary.
        else:

            # This scenario indicates that a new filepath was hashed
            # as no earlier entry was found in the CSV dictionary.
            # This newly founded key-pair value will be added to the
            # new dictionary for use later in the program.
            dictNew[pathCurrent] = dictCurrent.get(pathCurrent)

            # TESTING LINE ONLY
            print("Found something new!", pathCurrent)

    # For loop to iterate through each key (path) in the CSV 
    # dictionary.
    for pathCSV in dictCSV:


        # Testing to see if a key that is present in the CSV  
        # dictionary is also present in the current dictionary.
        if pathCSV in dictCurrent:
            continue

        # This else indicates a key-pair value that is present in 
        # the original CSV file but not in the current dictionary.
        else:

            # This indicates that a file was removed and will assign
            # that key-pair (path-hashed) value to a "removed" 
            # dictionary that I will later use in the program.
            dictRMV[pathCSV] = dictCSV.get(pathCSV)

            # TESTING LINE ONLY
            print("Somehting was removed.")

    #---------------------Comparing Process End-------------------

def initialHashwithWrite():

    csv = open("lab08.csv", "w+")

    for root, dirs, files in os.walk("/", topdown=False):
        
        if "/usr" in root:
            indicator = 1

        elif "/boot" in root:
            indicator = 1

        elif "/bin" in root:
            indicator = 1
        
        elif "/etc" in root:
            indicator = 1

        elif "/dev" in root:
            indicator = 1

        elif "/proc" in root:
            indicator = 1
        
        elif "/run" in root:
            indicator = 1

        elif "/sys" in root:
            indicator = 1

        elif "/tmp" in root:
            indicator = 1
        
        elif "/var/lib" in root:
            indicator = 1

        elif "/var/run" in root:
            indicator = 1

        elif "/var/ossec/queue" in root:
            indicator = 1

    
        else:
            indicator = 0
            for name in files:
                
                path = os.path.join(root, name)
                fd = open(path, "rb")
                fdread = fd.read()
                hashed = hashlib.sha256(fdread).hexdigest()

                time = str(datetime.datetime.now())


                csv.write(path + "," + hashed + "," + time + "\n")

main()