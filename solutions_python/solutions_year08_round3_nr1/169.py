
def min_presses(P, K, L, freqs):
    min_presses = 0
    num_presses = 1
    
    for n in range(1, len(freqs)+1):
        f = freqs[n-1]
        min_presses += (f * num_presses)
        if n % K == 0:
            num_presses += 1
    return min_presses
    
def read_case(file):
    P, K, L = [int(n) for n in file.readline().strip().split()]
    freqs = [int(n) for n in file.readline().strip().split()]
    freqs.sort(reverse=True)
    return P, K, L, freqs

if __name__ == '__main__':
    import sys
    input_file = open(sys.argv[1])
    N = int(input_file.readline().strip())
    for i in range(1, N+1):
        print "Case #%d: %d" % (i, min_presses(*read_case(input_file)))

