import sys

def solve():
    N, U = map(int, sys.stdin.readline().rstrip().split())

    # Largest power of two lesser or equals U
    npt_k = 1<<(U.bit_length()-1)
    
    k = (N + 1 - npt_k) / npt_k

    a = npt_k * k - (N + 1 - 2*npt_k)
    b = (N + 1 - npt_k) - npt_k * k

    # There are a k's on the final row and b k+1's
    # This many users need to occupy stalls
    remainder = U - npt_k

    if remainder < b:
        # Final user will use a stall from b
        assert b != 0, 'WTF?'
        
        # Stall size is k+1
        min_gap = k//2
        max_gap = (k+1)//2
    else:
        # Finall user will get a stall from a
        min_gap = (k-1)//2
        max_gap = k//2
    
    return min_gap, max_gap


def main():
    T = int(sys.stdin.readline().rstrip())
    for t in range(1, T+1):
        min_gap, max_gap = solve()
        print 'Case #{}: {} {}'.format(t, max_gap, min_gap)

if __name__ == "__main__":
    main()
