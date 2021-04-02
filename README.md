# SY402-Lab08
( Yusuf Ahmad Azani )
( Section 4341 )

The hash.py program I have created is stored in "/var/www/html/lab08" and will produce the hashed output into "lab08.csv". 
Upon execution, the program can run based on two scenarios:

1) Initial Run - "lab08.csv" Does Not Yet Exist
  If the program is executed for the first time, it will walk through all the directories in the virtual machine and hash
  each file using the SHA256 hash function. The hashed output will be stored in a csv file titled "lab08.csv". Each line
  within said file will have three values seperated by a comma: the file path, the hashed output and the timestamp of
  the hash function.
 
2) Following Runs - "lab08.csv" Exists Within The Directory
  Using an if statement, the program will check for the existance of a .csv file from the initial program execution. Upon
  the detection of this file, it will conduct a "hash-and-compare" function. First, it will conduct the hashing function 
  throughout the directories to produce an updated version of the hashed output. This information is then stored in a
  dictionary named "dictCurrent". It will then compare the original file path and hashed values to the current values 
  and check for the any modifications, removals or additions to the sequence. This is done using a series of "if" statements.
  
 
