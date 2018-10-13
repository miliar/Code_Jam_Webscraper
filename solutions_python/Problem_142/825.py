import sys
f=open(sys.argv[1])
T=int(f.readline())
case=1
ans=0
while case<T+1:
    l=f.readline().split()
    N=int(l[0])

    strings=[]
    maxl=0
    minl=1000
    for n in xrange(N):
        s=f.readline().strip()
        if maxl<len(s):
            maxl=len(s)
        if minl>len(s):
            minl=len(s)
        strings.append(s)

    prev=""
    flag=False
    for string in strings:
        chars=[]
        for s in string:
            if len(chars)==0:
                chars.append(s)
            elif s != chars[len(chars)-1]:
                chars.append(s)

        if prev=="":
            prev="".join(chars)
        elif prev=="".join(chars):
            pass
        else:
            flag=True
            break

    if flag:
        print "Case #"+str(case)+": Fegla Won"
        case+=1
        continue


    #print prev

    count=[]
    i=0
    for string in strings:
        count.append([])
        si=0
        for p in prev:
            c=0
            while si<len(string):
                s=string[si]
                if s==p:
                    c+=1
                else:
                    break
                si+=1
            count[i].append(c-1)
            #print s
            #print count
        i+=1


    i=0
    maxar=[]
    while i<len(prev):
        maxc=0
        minc=10000
        for c in count:
            if maxc<c[i]:
                maxc=c[i]
            if minc>c[i]:
                minc=c[i]
        maxar.append(maxc-minc)
        i+=1

    #print maxar
    ans=sum(maxar)

    print "Case #"+str(case)+": "+str(ans)
    case+=1
