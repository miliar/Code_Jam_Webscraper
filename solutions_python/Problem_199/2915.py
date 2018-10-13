


def flip(s, p, i):
    
    for j in range(p):
        if s[i+j] == '+':
            s[i+j] = '-'
        else:
            s[i+j] = '+'
        


file = open('A-large.in', 'r')
ofile = open('output.txt', 'w')
a = file.read()
file.close()
b = a.split('\n')

cases = b[0]
for i in range(1, len(b)):
    if b[i] == '':
        continue
    print(b[i])
    s = list(b[i].split(' ')[0])
    p = int(b[i].split(' ')[1])
    count = 0
    for j in range(len(s)-p+1):
        if s[j] == '-':
            flip(s, p, j)
            count += 1
    if '-' in s:
        ans = 'IMPOSSIBLE'
    else:
        ans = count
    ofile.write('Case #'+str(i)+': ' + str(ans)+'\n')
ofile.close()