def process(filename):
    f = open(filename, 'r')
    o = open('output.out', 'w+')
    total_input = int(f.readline())
    for i in range(total_input):
        s = f.readline()
        n = int(s.split(' ')[0])
        k = int(s.split(' ')[1])
        res = check(n,k)
        if res == 1:
            o.write('Case #' + str(i+1) + ': ON\n')
        else:
            o.write('Case #' + str(i+1) + ': OFF\n')
    o.close()
    f.close()
        
def check(n,k):
    f = pow(2,n)-1
    inc = pow(2,n)
    while(f <= k):
        if ( k == f ):
            return 1
        else:
            f += inc
    return 0
    
    
if __name__ == "__main__":
    process('A-small-attempt2.in')