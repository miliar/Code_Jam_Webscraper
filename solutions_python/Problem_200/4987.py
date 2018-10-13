import sys

name = "B-small-attempt1"
path = "C:\Users\coola_000\Downloads\\"

sys.stdin = open(path + name + ".in", "r")
sys.stdout = open(name + ".out", "w")

testCases = int(sys.stdin.readline())

for testCase in range(1, testCases + 1):
    a = str(sys.stdin.readline().strip())
    if ''.join(sorted(a)) == a:
        print "Case #" + str(testCase) + ": " + a
    else:
        i = 0
        while i < len(a) and a[i] < a[i+1]:
            i+=1
        c = int(a[:i+1])
        b = ''
        if c > 1:
            c-=1
            b+=str(c)
        b+='9'*len(a[i+1:])
        print "Case #" + str(testCase) + ": " + b
