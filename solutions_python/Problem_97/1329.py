def alphabet(a, b):
    cnt = 0
    for i in range(a,b+1):
        h = set()
        z = str(i)
        for j in range(len(z)):
            x = int(z[j:]+z[0:j])
            if x not in h and x < i and x >= a:
                h.add(x)
                cnt += 1
    return cnt

if __name__ == "__main__":
    fn = open("C-large.in","r")
    tcase = int(fn.readline())
    for x in range(tcase):
        y = fn.readline()
        pp = y.split()
        print "Case #%d: %d" % (x+1, alphabet(int(pp[0]),int(pp[1])))
