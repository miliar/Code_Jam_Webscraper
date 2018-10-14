def solver(X, R, C):
    if X == 4 and R == 2 and C == 4:
        print "Exception!424"
        return "RICHARD"
    elif X == 4 and R == 4 and C == 2:
        print "Exception!442"
        return "RICHARD"
    else:    
        if R*C % X != 0:
            return "RICHARD"
    
        else:
            if max(R, C) >= X and min(R, C) >= (X+1)/2:
                return "GABRIEL"
            else:
                return "RICHARD"

def listmaker(words):
    list = []
    p = 0
    count = 0
    ind_n = words.count(' ')
    for n in range(0, len(words)):
        if count == ind_n:
            list.append(int(words[p:len(words)]))
            return(list)
            break
        else:
            for n in range(0, len(words)):
                if words[n] == " ":
                    list.append(int(words[p:n]))
                    count = count + 1
                    p = n + 1
                    
def readandwrite():
    inputtxt = open('/Users/yongeun/Dropbox/Code_Jam_2015/D-small-attempt1.in','r')
    outputtxt = open('/Users/yongeun/Dropbox/Code_Jam_2015/D-small-attempt1.out','w')
    T = int(inputtxt.readline())
    for k in range(0, T):
        line = listmaker(inputtxt.readline())
        outputtxt.write('Case #'+str(k+1)+': '+solver(line[0],line[1],line[2])+'\n')    
        
readandwrite()