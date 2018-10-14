maxnormal={0:0,1:1,2:1,3:1,4:2,5:2,6:2,7:3,8:3,9:3,10:4,11:4,12:4,13:5,14:5,15:5,16:6,17:6,18:6,19:7,20:7,21:7,22:8,23:8,24:8,25:9,26:9,27:9,28:10,29:10,30:10}
maxsurprising={0:0,1:1,2:2,3:2,4:2,5:3,6:3,7:3,8:4,9:4,10:4,11:5,12:5,13:5,14:6,15:6,16:6,17:7,18:7,19:7,20:8,21:8,22:8,23:9,24:9,25:9,26:10,27:10,28:10,29:10,30:10}

def presmetaj(n,s,p,tp):
    tp.sort(reverse=True)
    res = 0    
    for i in range(n):
        if (maxnormal[tp[i]] >= p):
            res+=1 
            continue
        if (s != 0):
            s-=1;
            if (maxsurprising[tp[i]] == p):
                res+=1
        else:
            break
    return res

def presmetajs(s):
    ns = [int(x) for x in s.split()]
    n = ns[0]
    s = ns[1]
    p = ns[2]
    tp = ns[3:]
    return presmetaj(n,s,p,tp)

f = open('input', 'rU')
f2 = open('output', 'w')
r = ''
for i in range(int(f.readline())):
    r+='Case #' + str(i+1) + ': ' + str(presmetajs(f.readline())) + '\n'
f2.write(r)
f.close()
f2.close()