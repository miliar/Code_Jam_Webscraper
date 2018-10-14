def mul(list):
    a = 1
    for i in list:
        a = a*i
    return a

def main():
    fi = open('A-small-attempt0.in')
    fo = open('A-small-attempt0.out', 'w')
    t = int(fi.readline())
    
    for i in range(t):
        ans = []
        c, l = fi.readline().strip().split(' ')
        p = fi.readline().strip().split(' ')
        
        c = int( c )
        l = int( l )
        
        
        for j in range(len( p )):
            p[j] = float( p[j] )
        
        
        # Case 1
        ln = l-c+1
        lp = mul(p)
        a = (ln * lp) + ( (ln+l+1) * (1-lp) )
        ans.append(a)
        
        # Case 3
        ans.append(1 + l + 1)
        
        # Case 2
        j = -1
        while( (j != ((l*-1)-1)) and (j > (c*-1))):
            ln = l-c+1+(-1*j)+1
            lp = mul(p[:j])
            a = (ln * lp) + ( (ln+l+1) * (1-lp) )
            ans.append(a)
            j = j - 1;
            
            
        #print ans
           
        fo.write("Case #%d: %f\n" % (i+1, min(ans)))
        print "Case #%d: %f" % (i+1, min(ans))        

if __name__ == "__main__":
    main()