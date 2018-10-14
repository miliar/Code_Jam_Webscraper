'''
Created on 2009-7-10

@author: roamer
'''
finalResult = 0
def containLetter(arr,char,index):
    ret = []    
    for i in arr:
        if dic[i][index] == char:
            ret.append(i)
        i += 1
    return ret
        
def getCase(str):
    ret = []
    while len(str):
        c = str[0]
        if c == '(':
            index = str.index(')')
            ret.append(list(str[1:index]))
            str = str[index + 1:]
        else:
            ret.append(list(c))
            str = str[1:]
    return ret

def processCase(str):
    global finalResult
    finalResult = 0
    parts = getCase(str)
    iteration(list(range(D)),parts, 0)
    return finalResult

def iteration(arr,parts,index):
    if index == L - 1:
        for c in parts[index]:
            for i in arr:
                if c == dic[i][index]:
                    global finalResult
                    finalResult += 1
                    break
    else:
        for c in parts[index]:
            larr = containLetter(arr, c, index)
            if len(larr) == 0:
                continue 
            iteration(larr, parts, index + 1)

if __name__ == "__main__":
    
    dic = []
    f = open('../datain/alien_language.txt','r')
    L,D,N = map(int,f.readline().strip().split(' '))
    i = 0
    while i < D:
        str = f.readline().strip()
        dic.append(str)
        i += 1
    i = 0
    while i < N:
        str = f.readline().strip()
        i += 1
        print("Case #%d: %d" % (i,processCase(str)))
    f.close()