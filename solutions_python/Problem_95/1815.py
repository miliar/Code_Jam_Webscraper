# skeleton

import sys

files = ["A-small-in","A-small-attempt0.in","A-large-practice.in"]
content = file(files[1])
cases = int(content.readline())

filename = "output.txt"
File = open(filename,'w')

mapping = {" ":" ", 'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c',
           'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g',
           'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n',
           't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q'}

for i in range(cases):
    current = content.readline().strip().lower()
    outputstr = ''
    for letter in current:
        outputstr = outputstr + mapping[letter]
    #print(outputstr)
    
    File.write("Case #%d: %s" % (i+1, outputstr) + "\n")


File.close()
