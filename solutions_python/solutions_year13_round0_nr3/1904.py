#!/usr/bin/python


inName = "C-small-attempt0.in"
outName = "C-small-attempt0.out"

inFile = open(inName, 'r')
inData = inFile.readlines()
inFile.close()

#print inData

outFile = open(outName, 'wt')

numTest = int(inData[0].replace('\n',''))
r = 1



def isPalindrome(n):
    orig = n
    total_len = len(str(n))
    cur_len = 1
    rst = 0
    while n > 0:
        rst += n%10 * 10**(total_len - cur_len)
        cur_len += 1
        n /= 10
    if (orig == rst):
        return 1
    else:
        return 0


def isSquare(n):
    if (0 == n**0.5 % int(n**0.5)):
        return 1
    else:
        return 0
    





for num in range(numTest):
    ran = inData[r].replace('\n','').split(' ')
    r += 1
    cnt = 0
    for i in range(int(ran[0]), int(ran[1])+1):
        if ( 1 == isPalindrome(i)):
            if ( 1 == isSquare(i) ):
                if ( 1 == isPalindrome(int(i**0.5))):
                    cnt += 1
    print cnt
    
    outFile.write("Case #"+str(num+1)+": ")
    
    outFile.write(str(cnt))

    outFile.write("\n")
    





















