def number(S):
    d={}
    for i in range(10):
        d[i]=0
    d[0]=S.count('Z')
    d[6]=S.count('X')
    d[2]=S.count('W')
    d[8]=S.count('G')
    d[4]=S.count('U')
    if 'R' in S:
        d[3]=S.count('H')-d[8]
    if 'F' in S:
        d[5]=S.count('F')-d[4]
    if 'V' in S:
        d[7]=S.count('V')-d[5]
    if 'O' in S:
        d[1]=S.count('O')-d[2]-d[4]-d[0]
    if 'I' in S:
        d[9]=S.count('I')-d[5]-d[8]-d[6]
    l=[]
    for i in d.keys():
        l.append(str(i)*d[i])
    l.sort()
    return ''.join(l)
q=[]
for k in  range(input()):
    q.append(raw_input())
for x in range(len(q)):
    print 'Case #'+str(x+1)+': '+number(q[x])
        
