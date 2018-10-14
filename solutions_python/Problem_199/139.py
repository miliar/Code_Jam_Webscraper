import Queue
filename = "C:\\Users\\Andri_000\\Downloads\\python\\codejam2017\\Round Qualification\\A\\A-large"


fin = open(filename+".in")
fout = open(filename+".out","w")
trials = int(fin.readline())


def transform(s, j, k):
    dic = {"+":"-", "-":"+"}
    ans = ""
    for i in range(len(s)):
        if (i < j or i >= j + k):
            ans += s[i]
        else:
            ans += dic[s[i]]
    return ans


for T in xrange(trials):
    
    pcks, k = fin.readline().split(' ')
    l, k = len(pcks), int(k)
    flag = False
    step = 0
    
    q = Queue.Queue()
    q.put(pcks)
    
    while not flag:
        s = q.get()
        i = 0
        if s[0] == '-':
            s = transform(s, 0, k)
            step += 1
        while (i < len(s) and s[i] == '+'):
            i += 1
        s = s[i:]
        if len(s) >= k:
            q.put(s)
        else:
            flag = True
    
    if s.count("-") == 0:
        fout.write("Case #{0}: {1}\n".format(T+1, step))
    else:
        fout.write("Case #{0}: IMPOSSIBLE\n".format(T+1))
    
    
                    
fin.close()
fout.close()