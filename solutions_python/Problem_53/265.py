def snap(N,K):
    bin_max = 2**N
    last = K % bin_max
    return 'ON' if last == bin_max - 1 else 'OFF'

def print_res(caseno,res):
    print "Case #%d: %s" %(caseno,res) 

def main():
    for case in xrange(1,int(raw_input())+1):
        N,K = [long(w) for w in raw_input().split(' ')]
        print_res(case,snap(N,K))

if __name__=="__main__":
    main()
