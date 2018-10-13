import sys
temp = map(int, sys.stdin.readline().split())
l, d, n = temp[0], temp[1], temp[2]
#print l,d,n

words = []
for i in range(d):
    words.append(sys.stdin.readline().strip())
words.sort()
#print(words)

def match(a, b):
    for x, y in zip(a, b):
        if x not in y:
            return False
    return True

for i in range(1, n+1):
    temp = sys.stdin.readline().strip()
    word = []
    brack = False
    for c in temp:
        if c == "(":
            brack = True
            word.append("")
        elif c == ")":
            brack = False
        elif brack:
            word[-1] = word[-1] + c
        else:
            word.append(c)
    print "Case #%d: %d" % (i, len([True for a in words if match(a, word)]))


