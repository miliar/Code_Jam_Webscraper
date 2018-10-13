from sys import stdout
#from nltk.corpus import wordnet
import re

i=0
counter=1
flag=0
error=0
mylist=list()

g2e = {'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o', 'f': 'c',
       'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g',
       'm': 'l', 'n': 'b', 'o': 'k', 'p': 'r', 'q': 'z', 'r': 't',
       's': 'n', 't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm',
       'y': 'a', 'z': 'q', ' ': ' '}
try:
    number=input()
except :
    print "Error: First line should be Number of Test Cases"
    number=0
    error=1

if(0 < number <= 30):
    while i<number:
        flag=0
        g=raw_input()
        mylist.append(g)
        i= i + 1

    for line in mylist:       
        index = 0
        flag=0
        stdout.write("Case #"+ str(counter)+": ")
        if len(line)==0:
            stdout.write("Error: Empty String")
            flag=1
        elif len(line)>100:
            stdout.write("Limit #2: G contains at most 100 characters.")
            flag=1
        if line.startswith(" "):
            stdout.write("Error: Sentence should not start with space.")
            flag=1
        if line.endswith(" "):
            stdout.write("Error: Sentence should not end with space.")
            flag=1
        if re.search('[0-9\!\@\#\$\%\^\&\*\(\)\_\+\-\=\`\~\,\.\<\>\/\?\;\'\:\"\[\]\{\}]', line):
            stdout.write("Error: Sentence should have only alphabets and spaces.")
            flag=1
        if not line.islower():
            stdout.write("Error: Characters should be in lower case.")
            flag=1
        if "  " in line:
            stdout.write("Error: More than one space adjacently used.")
            flag=1
##        words =line.split()
##        for word in words:
##            if wordnet.synsets(word) and len(word)>2:
##                  stdout.write("Limit #3: None of the text is guaranteed to be valid English.")
##                  flag=1
##                  break
        if flag==0:
            while index < len(line): 
                letter = line[index]
                stdout.write(g2e[letter])
                index = index + 1
        print
        counter = counter + 1
else:
    if error==0:
         print "Limit #1: 1 <= T <= 30. Where T is number of test cases"
   


        

