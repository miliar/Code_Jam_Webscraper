def init_m(m):
    m_new = list()
    for line in m:
        tmp = list()
        for i in line.strip():
            tmp.append(int(i))
            
        m_new.append(tmp)
        
    return(m_new)

def row2number(row):
    n = len(row)
    while n >= 0:
        if row[n-1] == 1:
            return n-1
        n -= 1

    return n

def distinct(t):
    t_new = list()
    tmp = set()
    for i in t:
        if i not in tmp:
            t_new.append(i)
        else:
            while i in tmp:
                i += 1
            t_new.append(i)
            
    return(t_new)
    
def check(t):
    for i in range(len(t)):
        if t[i] > i:
            return False
        
    return True

def down(t):
    max_t = max(t)
    loc = t.index(max_t)
    tmp = t.pop(loc)
    
    count = tmp - loc
    if count < 0: count = 0
    
    return t, count

def min_row_change(m):
    
    t = list()
    for i in m:
        t.append(row2number(i))
            
    t = distinct(t)
    
    count = 0
    while not check(t):
        t, tmp = down(t)
        count += tmp
        
    return count

def main(filename, out = 'result.txt'):
    rfile = open(filename)
    wfile = open(out, 'w')
    
    rfile.readline()
    f = rfile.readlines()
    case = 0
    while f:
        case += 1
        N = int(f[0].strip())
        f = f[1:]
        ws = f[0:N]
        f = f[N:]
        m = init_m(ws)
        count = min_row_change(m)
        wfile.write('Case #'+str(case)+': '+str(count)+'\n')
    
if __name__ == '__main__':
    import sys
    #import psyco
    #psyco.full()
    in_file = sys.argv[1]
    main(in_file) 