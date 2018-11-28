import sys

if __name__ == '__main__':
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)
    output = open('danout.out', 'w')
    t = int(f.readline())
    for test in xrange(1, t+1):
        c = 0
        str1 = "Case #%d: " %(test)
        output.write(str1)
        arr = map(int, f.readline().strip().split())
        n = arr[0]
        s = arr[1]
        p = arr[2]
        goog = arr[3:]
        goog.sort()
        fl=0
        y = 0
        for k in goog:
            temp = k-p
            temp/=2
            if fl==1 and k>=y:
                c+=1
            elif temp >= p-1 and temp>=0:
                c+=1
                fl=1
                y=k
            elif temp >= p-2 and s>=1 and temp>=0:
                c+=1
                s-=1
        output.write(str(c)+"\n")
    output.close()
