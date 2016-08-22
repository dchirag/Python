


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
Problem 8.4

8.4 Open the file romeo.txt and read it line by line. For each line,
 split the line into a list of words using the split() method. The program should build a list of words. 
 For each word on each line check to see if the word is already in the list and if not append it to the list.
 When the program completes, sort and print the resulting words in alphabetical order.

 Desired output:
 ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']


'''


fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	line = line.rstrip()
	word_in_line = line.split(" ")
	for word in word_in_line:
    		if word not in lst:
            		lst.append( word )
    
lst.sort()
print lst

