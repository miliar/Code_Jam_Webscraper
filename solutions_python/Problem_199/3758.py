def out(x, y):
    outString = "Case #"+str(x)+": "+str(y)+'\n'
    file = open("output.txt","a")
    file.write(outString)
    file.close()

def check(s,y):
    for letter in s:
        if letter == "-":
            return "IMPOSSIBLE"
    return y

def swap(x):
    if x == "+":
        return "-"
    else:
        return "+"

def flip(s, i):
    new = s
    i = int(i)
    k = 0
    pos = 0
    y = 0

    while pos <= len(s) - i:
        if s[pos] == "-":
            y+=1
            k = pos
            while k < pos+i:
                s = s[:k] + swap(s[k]) + s[k+1:]
                k+=1
        pos+=1
    return check(s, y)
    

def generate(s):
    file = open(s, 'r')
    open("output.txt", "w").write("")
    i = 1
    for line in file:
        if len(line.split(" ")) < 2:
            pass
        else:
            word, number = line.split(" ")
            out(i, flip(word, number))
            i+=1
    file.close()
        

generate("A-large.txt");

