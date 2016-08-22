'''
    This code is written to fulfil coursera assignment for the coursera
        Python Data Structures
        University Of Michigan, Prof. Charles Severance
        Aug 2016
   
   It is written with my own efforts and settings. You are free to use it for non-coursera works. 
   However, it is copywrighted material and seek my persmission and coursera permission for test Datasets

   Author: Chirag Desai


'''


'''
Problem statement:

9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

uses: mb.txt by coursera 


'''


name = "mb.txt"
emap = dict()
   
handle = open(name)

for line in handle.readlines():
    	if line.startswith( "From "):
                broken = line.split(" ")
                ename = broken[1]
                #print ename
                if 	ename in emap :
                        emap[ename] = emap[ename]+1
                else: 
                        emap[ename] = 1
      
                    
#print emap
max = 0
max_emailer = "No emails found"

for n , v in emap.items():
    print n , v
    if v > max :
        max_emailer = n
        max = v

print "Maximum emails by" , max_emailer, "with count", emap[max_emailer] 