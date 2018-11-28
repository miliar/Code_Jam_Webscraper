import sys
sys.stdout=open("/Users/ahanaghosh/Documents/Abhirup/python/out.rtf","w")

def checkIfSorted(numList):
    b = numList
    l = len(b)
    flag = False
    prevDigit = b[0]
    i = 1
    while i<l:
        if prevDigit <= b[i]:
            flag = True
            prevDigit = b[i]
        else:
            flag = False
            break
        i = i+1
    return(flag)
        
    
def solve(b):
    digiList = list(str(b))
    d = len(digiList)

    if d==1:
        return(b)
    
    digiList = list(map(int, digiList))
    #print("2. Solve (Start) with num=",digiList)
    if checkIfSorted(digiList)==True:
        return(b)
    else:
        prevDigit = digiList[0]
        i = 1
        while i<d:
            if prevDigit > digiList[i]:
                #print("Number is ",digiList)
                digiList[i-1] = prevDigit-1
                n = i
                while n<d:
                    digiList[n]=9
                    n = n+1
                break
            else:
                prevDigit = digiList[i]
                i = i+1
        num = ''.join(map(str, digiList))
        return (solve(int(num)))
    

#Convert list of strings to number
#b = list(map(int, b))
#b = ''.join(map(str, b))

with open("/Users/ahanaghosh/Documents/Abhirup/python/path.in") as f:
    mylist = f.read().splitlines()
mylist = list(map(int, mylist))


t = mylist[0]

for x in range(0, t):
    n = mylist[x+1]
    d = len(str(n))
    y = int(n)
    z = solve(y)
    print("Case #",x+1,":", z, sep = '')

sys.stdout.close()



