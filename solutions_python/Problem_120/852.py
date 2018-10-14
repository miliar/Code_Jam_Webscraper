
def numrings(R, T):
    inr = R
    outr = R+1
    inksofar = 0
    ringarea = outr**2 - inr**2
    inkwithnext = inksofar + ringarea
    cnt = 0
    while(inkwithnext <= T):
        cnt = cnt+1
        inksofar = inkwithnext
        inr = inr + 2
        outr = outr + 2
        ringarea = outr**2 - inr**2
        inkwithnext = inksofar + ringarea
    return cnt

if __name__ == "__main__":
    infile = open('A-small-attempt1.in', 'r')
    outfile = open('A-small.out', 'w')
    string = infile.readline()
    T = int(string)
    for i in range(1, T+1):
        string = infile.readline()
        parts = string.rsplit(' ')
        r = int(parts[0])
        t = int(parts[1])
        print r
        print t
        num = numrings(r, t)
        print num
        outfile.write('Case #'+str(i)+': '+str(num)+'\n')

    infile.close()
    outfile.close()

    
