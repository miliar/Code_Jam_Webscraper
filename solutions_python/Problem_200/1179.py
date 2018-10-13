import string

def sol(s):
    s = [c for c in str(s)]
    curr = -1
    i = 0
    while int(s[i]) >= curr:
        curr = int(s[i])
        i += 1
        if i == len(s):
            return ''.join(s)
    if int(s[i]) < curr:
        while i-2>= 0 and s[i-2] == s[i-1]:
            i -= 1
        s[i-1] = str(int(s[i-1])-1)
        for j in range(i,len(s)):
            s[j] = '9'
    if s[0] == '0':
        s = s[1:]
    return ''.join(s)



fIn = open('input.in', 'r')
fOut = open('output.txt', 'w')
case = 0
for line in fIn:
    print(case)
    if case > 0:
        k = int(line.split()[0])
        fOut.write("Case #"+str(case)+": "+str(sol(k))+"\n")
    case += 1