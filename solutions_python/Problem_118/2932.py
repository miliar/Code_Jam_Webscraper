inFile = open('C-small-attempt0.in')
out = open("out.txt","w")
numcase = int(inFile.readline())
n = 1
import math

def test(s):
    if s == '' or len(s) == 1:
        return True
    else:
        if s[0] == s[-1]:
            return test(s[1:-1])
        else:
            return False
while n <= numcase:
    s = inFile.readline().split()
    small = int(s[0])
    big = int(s[1])
    num = 0
    for i in range(small,big+1):
        if len(str(i)) > 1 and not test(str(i)):
            continue
        else:
                
            sq = math.sqrt(i)
            if len(str(i)) == 1:
                if sq < 10 and (int(sq))**2 == i:
                    num += 1
            else:
                if sq < 10 and (int(sq))**2 == i:
                    num += 1
                else:
                    if test(str(int(sq))) and (int(sq))**2 == i:
                        num += 1
    out.write("Case #"+str(n)+": %d\n" % (num) )
            

    n += 1
inFile.close()
out.close()
