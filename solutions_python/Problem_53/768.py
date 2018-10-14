input_file = 'A-large.in'

def main():
    fin = open(input_file, 'r', 0)
    T = int(fin.readline())
    for i in range(T):
        N, K = fin.readline().split(' ')
        if (int(K) % (2 ** int(N))) == 2 ** int(N) - 1:
            t = 'ON'
        else:
            t = 'OFF'
        print "Case #%d: %s" % (i+1, t)

main()
