import os
f = open(os.path.expanduser("./B-small-attempt0.in"))

def chk(num):
    c = 9
    while(num > 0) :
        b = num % 10
        if(b > c):
            return False
        else:
            c = b
        num /= 10
    return True
t = int(f.readline())
for i in range(t):
    v = int(f.readline())
    flg = True
    while(v > 0):
        if(chk(v)):
            print ('Case #'+repr(i+1)+': '+repr(v))
            break
        else:
            v -= 1
f.close()