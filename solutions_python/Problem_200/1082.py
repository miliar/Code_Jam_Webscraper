


def transform(tab):
    #print tab
    if len(tab) == 1:
        return tab
    i = 1
    n = len(tab)
    while i < n and tab[i] >= tab[i - 1]:
        i += 1
    if i == n:
        return tab
    idx = i
    #print tab
    #print i
    bak = -1
    comp = tab[i-1]
    #if (i == 1):
    #    tab[i - 1] = str(int(tab[i - 1]) - 1)
    #else:
    #    bak = tab[i - 1]
    #    tab[i - 1] = tab[i]
    i -= 1
    
    while i > 0 and tab[i] == comp:
        #if i == 0:
        #    tab[i] = str(int(tab[i]) - 1)
            
        #else:
        #    bak = tab[i - 1]
        #    tab[i - 1] = tab[i]
        i -= 1
    if tab[i] == comp:
        tab[i] = str(int(tab[i]) - 1)
        s = i
    else:
        tab[i + 1] =  str(int(tab[i + 1]) - 1)
        s = i + 1
   
    if tab[s] == '0':
        # all 9
        tab = (n-1) * ['9']
    else:
        # all from idx 9
        for j in range(s+1, n):
            tab[j] = '9'
    return tab

if __name__ == "__main__":
    
    f = open("input.txt")
    lines = f.readlines()
    f.close()
    t = int(lines[0])
    i = 1
    while i <= t:
        s = lines[i].strip()
        #print s
        res = transform(list(s))
        
        print "Case #%d: %s" % (i, ''.join(res))
        i += 1
    
