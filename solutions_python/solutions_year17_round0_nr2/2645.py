import time

def functionForLine(line):
    intList = list(str(line))
    intList = [int(i) for i in intList]
    print("Line: " + str(line))
    
    for i in range(len(intList)-1,0,-1):
        if intList[i-1]>intList[i]:
            intList[i-1]-=1
            for k in range(i,len(intList)):
                intList[k] = 9

    intList = [str(i) for i in intList]
    line=str(int("".join(intList))) 
    print("Line: " + str(line))
    
    return str(line)

with open("B-large.in") as f:
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



