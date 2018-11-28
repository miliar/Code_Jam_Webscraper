num = input()
for i in range(num):
    case = input()
    j = case
    digitInd = 0
    while 1:
        s = str(j)[::-1]
        if all(s[i]>=s[i+1] for i in range(len(s)-1)):
            print "Case #%d: %d"%(i+1,j)
            break
        pos = 10**digitInd
        j-=pos*(int(s[digitInd])+1)
        digitInd+=1
