import array

def gcd(x, y):
    if x < y:
        tmp = x
        x = y
        y = tmp

    if y==0:
        return x

    return gcd(y, x%y)           

if __name__=='__main__':
    C = int(raw_input())
    for i in range(C):
        str = raw_input()
        s = str.split()
        N = int(s[0])
        diff = []
        for j in range(N-1):
            diff.append(abs(int(s[j+2])-int(s[j+1])))
        
        gcdtmp = -1

        for j in range(N-1):
            if diff[j] != 0:
                if gcdtmp<0:
                    gcdtmp = diff[j]
                else:
                    gcdtmp = gcd(gcdtmp, diff[j])

        if int(s[1])%gcdtmp == 0:
            y = 0;
        else:
            y = gcdtmp - (int(s[1]) % gcdtmp)

        print "Case #%d: %d" %(i+1, y)

