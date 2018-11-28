#!/usr/bin/python3

def fairAndSquare() :
    fread = open("C-small-attempt0.in","r")
    fwrite = open("output.txt","w")
    x = int(fread.readline())
    squares = []
    fairandsquare = {}
    i = 1
    square = 1
    while ( square <= 1000):
        squares.append(square)
        i += 1
        square = i * i

    for k in range(1,i):
        if(checkPalindrome(k) and checkPalindrome(squares[k-1])):
            fairandsquare[squares[k-1]]=k

    for aa, bb in fairandsquare.items():
        print(aa, bb)

    for j in range(0,x):
        line = fread.readline()
        count = 0
        newlineindex = line.find("\n")
        exactvalue = line[:newlineindex]
        arr = exactvalue.split(" ")
        a = int(arr[0])
        b = int(arr[1])
        for p in range(a,(b+1)):
            if(p in fairandsquare):
                count += 1
        val = str(count)
        index = str(j+1)
        fwrite.write("Case #" + index + ": " + val)
        fwrite.write("\n")


    fread.close()
    fwrite.close()

def checkPalindrome(n):
    flag = True
    origvalue = n
    while(n>0):
        power = len(str(n))-1
        if((n % 10) != int(n/(10 ** power))):
            flag = False
        n = n % (10 ** power)
        n = int(n/10)
    if(flag):
      print(str(origvalue)+" is a palindrome")
    else :
        print(str(origvalue)+"is not a palindrome")  
    return flag    
            

if __name__ == "__main__":
    fairAndSquare()
