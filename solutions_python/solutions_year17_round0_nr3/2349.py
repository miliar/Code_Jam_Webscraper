#!python
def solve(n, k):
    #print(n, k)
    if k == 0:
        return 1e18, 1e18
    if n == k:
        return 0, 0
    if k == 1:
        if n % 2 == 0:
            big = n/2
            small = n/2 - 1
        else:
            big = n//2
            small = n//2            
        return big, small
    else:
        if (k-1)%2 == 0:
            nk = (k-1)/2
            if (n-1)%2 == 0:
                nn = (n-1)/2
            else:
                nn = n/2 - 1
            return solve(nn, nk)
        else:            
            if (n-1)%2 == 0:
                nk = k/2
                nn = (n-1)/2
                return solve(nn, nk)
            else:
                a1,b1 = solve(n/2, k/2)
                a2,b2 = solve(n/2-1, k/2-1)
                if b1 < b2:
                    return a1, b1
                else:
                    return min(a1,a2), b1
                
        return solve(nn, nk)
    

def main():
    t = int(input())
    for c in range(1, t + 1):
        n, k = map(int,input().split(' '))
        a,b = solve(n, k)
        print('Case #%d: %d %d' % (c, a, b))
    
if __name__ == "__main__":
  main()
    