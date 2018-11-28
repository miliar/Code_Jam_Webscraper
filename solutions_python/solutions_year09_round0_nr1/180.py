ttt=raw_input();
ttt=[int(x) for x in ttt.split(' ')]
l=ttt[0]
d=ttt[1]
n=ttt[2]
words=[]
for i in range(d):
    tt=raw_input()
    words.append(tt)
for i in range(n):
    s=raw_input()
    a=[]
    for j in range(l):
        a.append([])
    paren=False
    ctr=0
    for j in range(len(s)):
        if s[j].isalpha():
            a[ctr].append(s[j])
            if not paren:
                ctr+=1
        if s[j]=='(':
            paren=True
        if s[j]==')':
            paren=False
            ctr+=1
    tot=0
    for j in range(d):
        flag=True
        for k in range(l):
            if words[j][k] not in a[k]:
                flag=False
                break
        if flag:
            tot+=1
    print 'Case #'+str(i+1)+': '+str(tot)
