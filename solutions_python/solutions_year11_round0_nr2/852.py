ln = '\n'
filename = 'a.in'
r = open(filename,'r')
w = open('out.txt','w')
t = int(r.readline())
k = 1
while k<=t:
    line = r.readline().strip().split()
    l_com = []
    n_com = int(line[0])
    for i in range(n_com):
        l_com.append(line[i+1])
    l_opp = []
    n_opp = int(line[1+n_com])
    for i in range(n_opp):
        l_opp.append(line[i+n_com+2])
    num = int(line[n_com+n_opp+2])
    ss = line[-1]
    """
    print n_com,
    for i in l_com:
        print i,
    print n_opp,
    for i in l_opp:
        print i,
    print num,ss
    """
    ll = []
    for i in ss:
        ll.append(i)
        if len(ll)>=2:
            temp = ''.join(map(str,ll[-2:]))
            kk = -1
            for j in l_com:
                if temp==j[:2] or temp==j[:2][::-1]:
                    kk = j[2]
                    break
            if kk!=-1:
                ll.pop()
                ll.pop()
                ll.append(kk)
            
            for j in l_opp:
                if j[0] in ll and j[1] in ll:
                    ll = []

    w.write('Case #%d: [' % k)
    w.write(', '.join(ll))
    w.write(']'+ln)

    k += 1

r.close()
w.close()

