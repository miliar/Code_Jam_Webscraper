def work(niz, iter, dict):
    global n
    if niz == "" and len(dict) > 0:
        n += 1

    elif niz[0] == "(":
        end = niz.find(")")
        for i in range(1,end):
            if iter==0:
                try:
                    work(niz[end+1:], iter + 1, dict[niz[i]])
                except:
                    pass
            else:
                #ce iter !=0
                T=[]
                for e in dict:
                    if e[iter] == niz[i]:
                        T.append(e)
                if len(T) > 0:
                    work(niz[end+1:], iter + 1, T)
                    #print T, iter+1, niz[end+1:]
                
    else:
        if iter==0:
            try:
                work(niz[1:], iter + 1, dict[niz[0]])
            except:
                pass
        else:
            # ce iter !=0
            T=[]
            for e in dict:
                if e[iter] == niz[0]:
                    T.append(e)
            if len(T) > 0:
                work(niz[1:], iter + 1, T)
                
        
            

a = open("A-large.in")
a = a.readlines()
L, D, N = [int(i) for i in a.pop(0).strip().split(" ")]
dict = {}
words = a[:D]
a = a[D:]
dict = {}
for e in words:
    try:
        dict[e[0]] += [e.strip()]
    except:
        dict[e[0]] = [e.strip()]
        
for i in range(N):
    n = 0
    niz = a.pop(0).strip()
    work(niz, 0, dict)
    print "Case #"+str(i+1)+":", n


