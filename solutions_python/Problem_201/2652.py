#pC qualification round

#brute force to start out with
def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n, m = [int(s) for s in raw_input().split(" ")]
        solve(n, m, i)

def solve(n, k, ind):
    stalls = [1] + [0] * n + [1]

    max1 = 0
    min1 = 0
    
    for i in range(k):
        lengths = []
        lengths_indices = []
        last_ind = 0
        
        for j in range(1, len(stalls)):
            if stalls[j] is 1:
                lengths.append(j - last_ind - 1)
                lengths_indices.append((last_ind + j) // 2)
                last_ind = j
                
                max1 = (last_ind + j + 1) // 2
                min1 = (last_ind + j) // 2

        stalls[lengths_indices[lengths.index(max(lengths))]] = 1
        min1 = (max(lengths) - 1) // 2
        max1 = max(lengths) // 2
        
    print "Case #%i: %i %i" % (ind, max1, min1)
        
main()
