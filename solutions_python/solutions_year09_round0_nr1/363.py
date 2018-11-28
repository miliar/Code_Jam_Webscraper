import pprint
import re

if __name__ == "__main__":
    fin  = open('d:\\a.in', 'r')
    fout = open('d:\\a.out', 'w')
    line = fin.readline().split()
    L = int(line[0])
    D = int(line[1])
    N = int(line[2])
    dic = []
    for i in range(D):
        dic.append(fin.readline().strip())
        
    for i in range(1, N+1):
        print('Line %d' % i)
        line = fin.readline().strip()
        r = '';
        inBrace = False
        j = -1
        ar = []
        ar_i = {}
        for c in line:
            if c == '(':
                inBrace = True
                j += 1
                ar.append([])
                ar_i.update({j:0})
            elif c == ')':
                inBrace = False
            else:
                if not inBrace:
                    j += 1
                    ar.append([])
                    ar_i.update({j:1})
                ar[j].append(c)
                if inBrace:
                    ar_i[j] += 1
        
        items = ar_i.items()
        items = [(v, k) for (k, v) in items]
        items.sort()
        items = [(k, v) for (v, k) in items]
        
        valid = [True for j in range(D)]
        result = D
        
        #pprint.pprint(ar)
        #pprint.pprint(items)
        #pprint.pprint(dic)
        
        for j in items:
            for k in range(len(dic)):
                if valid[k]:
                    if not dic[k][j[0]] in ar[j[0]]:
                        valid[k] = False
                        result -= 1                        
        
        fout.write('Case #%d: %d\n' % (i, result))

  