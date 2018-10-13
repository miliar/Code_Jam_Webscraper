
fin = open("C-large.in", "r")
fout = open("C-large.out", "w")


def main():
    
    square = [1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004]    
    N = int(fin.readline())
    for n in xrange(1,N+1):
        fout.write("Case #%i: " %(n))
        P = fin.readline().split()
        S,B = long(P[0]), long( P[1]) #S,B are the limits
        
        count = 0
        for i in square:
            if i >= S and i <= B:
                count = count+1
        print count        
        fout.write("%i \n" %(count))        

    fout.close()

if __name__ == '__main__':
    main()
