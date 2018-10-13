o = open('out', 'w')

f = open('in')
lines = f.readlines()

N = int(lines.pop(0))
res = 1

for num in xrange(1, N+1):
    engines = []
    queries = []
    qEngs = []
    dict = {}
    switch = 0
        
    Neng = int(lines.pop(0))
    for i in xrange(Neng):
        engines.append(lines.pop(0))
        
    Nquer = int(lines.pop(0))
    for i in xrange(Nquer):
        queries.append(lines.pop(0))

    def clear():
        for e in engines:
            dict[e]=0
            
    clear()
    #unify
    if len(queries):
        past = queries[0]
        nu = []
        nu.append(past)
        for q in queries:
            if q!=past:
                nu.append(q)
            past=q
            queries = nu
        
        nq = len(queries)
        def recurse(q,ls):
           # print q,ls
            while 1:
                if ls == []:
                    break
                
                global switch
                clear()
                if q!=None:
                    dict[q]=1
                s = len(ls)
                i = 0
            
                while 1:
                    r = ls[i]
                    dict[r]=1
                    if dict.values().count(0)==0:
                        switch+=1
                        clear()
                        q = r
                        ls = ls[i+1:]
                        break
                    i+=1
                    if i>s-1:
                        ls = []
                        break
                    
        recurse(None,queries)
    print 'Case #'+str(num)+':',switch

    
    