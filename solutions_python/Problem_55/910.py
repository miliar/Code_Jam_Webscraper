import collections
#filename="/users/stevemardenfeld/Documents/codejam/themepark/test.txt"

def t(filename,outfile):
    out = file(outfile,"w")
    f = file(filename)
    t = int(f.readline().strip())
    for i in range(t):
        run,people,gtotal= map(int,f.readline().strip().split())
        q = collections.deque(map(int,f.readline().strip().split()))
        total = 0
        for j in range(run):
            count=0
            intq = []
            while count<people and len(q)>0:
                if count+q[0]<=people:
                    count+=q[0]
                    intq.append(q.popleft())
                else:
                    break
            total+=count
            q.extend(intq)
        out.write("Case #%s: %s\n"%(i+1,total))
    out.close()
    
    
