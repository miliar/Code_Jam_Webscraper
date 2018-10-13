def solve():
    import Queue,bisect
    f=open("C-large.in")
    f2=open("output.txt",'w')
    lines=f.readlines()
    t=int(lines[0])
    # t=input()
    for test in xrange(1,t+1):
        n,k=map(int,lines[test].split())
        # n,k=map(int,raw_input().split())
        l=[(n//2,(n-1)//2)]
        d={l[0]:1}
        q=Queue.Queue()
        q.put(l[0])
        while not q.empty():
            popped=q.get()
            # print popped,d[popped]
            for x in popped:
                if x>0:
                    elem=(x//2,(x-1)//2)
                    if elem in d:
                        d[elem]+=d[popped]
                    else:
                        d[elem]=d[popped]
                        l.append(elem)
                        q.put(elem)
        # print l
        # print d
        person=[d[l[0]]]
        for x in l[1:]:
            person.append(person[-1]+d[x])
        # print person
        ans=l[bisect.bisect_left(person,k)]

        # print "Case #{}: {} {}\n".format(test,ans[0],ans[1])
        f2.write("Case #{}: {} {}\n".format(test,ans[0],ans[1]))
    f2.close()
    f.close()
solve()
