def flipChar(c):
    if c == '-':
        c = '+'
    else:
        c = '-'
    return c

def flip(line, index, width):
    #print(line)
    if (index + width) > len(line):
        raise Exception
    for i in range(index, index+width):
        line[i] = flipChar(line[i])
    return line
    
def checkLine(case,s):    
    line, width = s.split()
    width = int(width)
    line = [c for c in line]
    counter = 0
    #i = solved
    #j = not necessarily solved yet
    try:
        for i in range(len(line)):
            if line[i] == '+':
                continue
            else:
                line = flip(line, i, width)
                counter+=1
        print("Case #{}: {}".format(case +1, counter))
    except Exception:
        print("Case #{}: {}".format(case +1,"IMPOSSIBLE"))


for case in range(eval(input())):
    checkLine(case,input())

