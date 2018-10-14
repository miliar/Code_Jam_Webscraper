import re
s = raw_input()
s =  s.split(' ')
L = int(s[0])
D = int(s[1])
N = int(s[2])

dic = []
for i in range(D):
    dic += [raw_input().strip()]

for i in range(N):
    c = 0
    s = raw_input().strip()
    s = '^' + s.replace('(','[').replace(')',']') + '$'
    for j in range(D):
        c = c + len(re.findall(s, dic[j]))
    print ("Case #%d: " % (i+1)) + str(c)
