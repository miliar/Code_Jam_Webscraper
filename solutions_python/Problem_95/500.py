import sys

if __name__ == '__main__':
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)
    output = open('tongout.out', 'w')
    t = int(f.readline())
    for test in xrange(1, t+1):
        str1 = "Case #%d: " %(test)
        output.write(str1)
        string = f.readline().strip()
        ans = []
        for i in string:
            if i == 'a':
                ans.append('y')
            elif i == 'b':
                ans.append('h')
            elif i == 'c':
                ans.append('e')
            elif i == 'd':
                ans.append('s')
            elif i == 'e':
                ans.append('o')
            elif i == 'f':
                ans.append('c')
            elif i == 'g':
                ans.append('v')
            elif i == 'h':
                ans.append('x')
            elif i == 'i':
                ans.append('d')
            elif i == 'j':
                ans.append('u')
            elif i == 'k':
                ans.append('i')
            elif i == 'l':
                ans.append('g')
            elif i == 'm':
                ans.append('l')
            elif i == 'n':
                ans.append('b')
            elif i == 'o':
                ans.append('k')
            elif i == 'p':
                ans.append('r')
            elif i == 'q':
                ans.append('z')
            elif i == 'r':
                ans.append('t')
            elif i == 's':
                ans.append('n')
            elif i == 't':
                ans.append('w')
            elif i == 'u':
                ans.append('j')
            elif i == 'v':
                ans.append('p')
            elif i == 'w':
                ans.append('f')
            elif i == 'x':
                ans.append('m')
            elif i == 'y':
                ans.append('a')
            elif i == 'z':
                ans.append('q')
            elif i == ' ':
                ans.append(' ')
        out = ''.join(ans)
        output.write(out+"\n")
    output.close()
