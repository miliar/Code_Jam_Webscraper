
t = 0
fp = open("large.txt")  #input filename
fout = open("large_out.txt", "w") #output filename

    
def get_input():
    global t

    t = int(fp.readline())
    
    for i in xrange(t):
        line = fp.readline().split()
        r = int(line[0])
        c = int(line [0])
        tab = []
        for j in xrange(r):
            tab.append(fp.readline().strip())
        yield r,c,tab

def process(r,c, tab):
    for i in xrange(r-1):
        for j in xrange(len(tab[i])-1):
            ch = tab[i][j]
            #print i, j, tab[i+1]
            if ch == '#':
                if tab[i][j+1] == '#' and \
                   tab[i+1][j] == '#' and \
                   tab[i+1][j+1] == '#':
                    
                    tab[i] = tab[i][:j] + "/\\" + tab[i][j+2:]
                    tab[i+1] = tab[i+1][:j] + "\\/" + tab[i+1][j+2:]
                else:
                    #print tab[i], i, j,ch
                    return "Impossible"
        if "#" in tab[i]:
            return "Impossible"
    if "#" in tab[-1]:
        return "Impossible"
    return '\n'.join(tab)
    
for i,j in enumerate(get_input(), 1):
    r,c,tab = j
    #print n,tab
    r = process(r,c,tab)
    print "Case #%s:\n%s" % (i,r)
    print >> fout, "Case #%s:\n%s" % (i,r)
    
fout.close()
