import queue
import time

def functionForLine(line):
    text = line[0:line.find(" ")]
    K = int(line[line.find(" ") + 1: len(line)])
    
    soughtString = len(text)*"+"
    
    currDist = 0
    
    #print(text)
    
    for i in range(0, len(text)-K   +1):
        if text[i]=="-":
            text = flipN(text,i,K)
            currDist += 1
            #print(text)

    if text == soughtString:
        return str(currDist)
    else:
        return "IMPOSSIBLE"


def flipN(text, n, N):
    substring = text[n:n+N].replace("-", '!',)
    substring = substring.replace("+", "-")
    substring = substring.replace('!', "+")
    text = text[0:n] + substring + text[n + N: len(text)]
    return text


with open("A-large.in") as f:
    number_of_lines = int(f.readline())
    output = ""
    for i in range(1,number_of_lines+1):
        thisline = f.readline()
        thisline = thisline[0:len(thisline)-1]
        output += "Case #"+ str(i) + ": " + functionForLine(thisline) + "\n"
        
print()
print()
print()
print(output)
with open('largeoutput.in', 'w') as file:
    file.write(output)



