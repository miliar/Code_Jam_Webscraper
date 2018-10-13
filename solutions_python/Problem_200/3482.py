def solution(filename):
    lines = openFile(filename)
    n = eval(lines[0])
    lines = lines[1:]   
    count = len(lines)
    string = ""
    for i in range(len(lines)):
        string = string + "Case #" + str(i+1) + ": " + str(applyAlgorithm(eval(lines[i]))) + "\n"
        print((i/count)*100)  
    file = open("solution" + filename, "w")
    file.write(string)
    file.close

def openFile(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()  
    return lines
  

def applyAlgorithm(number):
    string = str(number)
    lastpos = len(string)-1
    for i in range(len(string)):
        if i != lastpos:
            if eval(string[i])>eval(string[i+1]):
                newstring = string[:i] + str(eval(string[i])-1) + (lastpos-i)*"9"
                if(newstring[0] == "0"):
                    newstring = newstring[1:]
                newnum = eval(newstring)
                if isTidy(newnum):
                    return newnum
                else:
                    return applyAlgorithm(newnum)
    return number

def isTidy(number):
    string = str(number)
    lastpos = len(string)-1
    for i in range(len(string)):
        if i != lastpos:
            if eval(string[i])>eval(string[i+1]):
                return False
    return True