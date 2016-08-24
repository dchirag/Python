'''
    This code is written to fulfil coursera assignment for the coursera
        Python Data Structures
        University Of Michigan, Prof. Charles Severance
        Aug 2016
   
   It is written with my own efforts and settings. You are free to use it for non-coursera works. 
   However, it is copyrighted material. Please notify me for usage and coursera permission for test Datasets

   -Chirag Desai


'''


'''
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.

You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt

'''

DEBUG=True

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
fcount = 0

if DEBUG:
    print fh    

for line in fh.readlines():
    if DEBUG:
        print line
    if line.startswith("From "):
            if DEBUG:
                print line
            fcount = fcount +1
            line = line.rstrip()
            broken_txt = line.split(" ")
            #print broken_txt
            print broken_txt[1]

    count = count + 1
    

print "There were", fcount, "lines in the file with From as the first word"



'''
Desired Output:
rjlowe@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
gsilver@umich.edu
gsilver@umich.edu
zqian@umich.edu
gsilver@umich.edu
wagnermr@iupui.edu
zqian@umich.edu
antranig@caret.cam.ac.uk
gopal.ramasammycook@gmail.com
david.horwitz@uct.ac.za
david.horwitz@uct.ac.za
david.horwitz@uct.ac.za
david.horwitz@uct.ac.za
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
louis@media.berkeley.edu
ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There were 27 lines in the file with From as the first word

'''