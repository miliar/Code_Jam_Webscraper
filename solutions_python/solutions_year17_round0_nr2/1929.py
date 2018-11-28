
def tidy(n):
    d = len(n)
    for i in range(d-1,0,-1):
        if n[i] < n[i-1]:
            n[i-1] = n[i-1] - 1
            fill(n,i)
    return sum(n[k]*10**(len(n)-k-1) for k in range(d))

def fill(n,k):
    for i in range(k,len(n)):
        n[i] = 9

if __name__ == "__main__":
    T = int(raw_input())
    for t in range(T):
        n = [int(c) for c in raw_input()]
        print "Case #{}: {}".format(t+1,tidy(n))
