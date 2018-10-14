code=open("code").readlines()
ls=open("A-small-attempt0.in").readlines()
#ls=open(".in").readlines()
T=int(ls[0])
case = 1
line = 1
googlerese = dict()
key = None
for i in range(len(code)):
    if i % 2 == 0:
        key = code[i][0]
    if i % 2 == 1:
        googlerese[key] = code[i][0]

while line < len(ls):
    ciph=ls[line]
    print "Case #%d:" % line,
    ans = ""
    for c in ciph:
        if c != ' ' and c != '\n':
            ans += googlerese[c]
        else:
            ans += c
    print ans,
    line += 1
