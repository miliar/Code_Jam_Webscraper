from math import *

code = {'y':'a','n':'b','f':'c','i':'d','c':'e','w':'f','l':'g','b':'h','k':'i','u':'j','o':'k','m':'l','x':'m','s':'n','e':'o','v':'p','z':'q','p':'r','d':'s','r':'t','j':'u','g':'v','t':'w','h':'x','a':'y','q':'z', ' ':' ','\n':'\n'}


output = open("output.txt", "wt")

text = open("sample.txt", "r")
textLines = text.readlines()

cases = int(textLines[0])
i = 0;

while i < cases:
    
    
    output.write("Case #"+str(i+1)+": ")
    message = textLines[i+1]
    j = 0
    newMessage = ""

    for j in range(len(message)):
        newMessage = newMessage + code[message[j]]
    output.write(newMessage)

    i = i + 1
    
