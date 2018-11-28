
def f(x):
    if x == 1:
        return 1
    return 1 + 2 * f(x-1)
    

if __name__ == "__main__":
    fin  = open('d:\\a.in', 'r')
    fout = open('d:\\a.out', 'w')
    T = int(fin.readline())
    for i in range(1, T+1):
        line = fin.readline().split()
        N = int(line[0])
        K = int(line[1])
        
        N = f(N) + 1
        K = K + 1
        if K % N:
            fout.write('Case #%d: OFF\n' % i)
        else:
            fout.write('Case #%d: ON\n' % i)