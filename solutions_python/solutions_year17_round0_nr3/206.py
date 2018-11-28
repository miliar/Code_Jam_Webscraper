
def is_power2(num):
	return num != 0 and ((num & (num - 1)) == 0)

def _solve(a,b,n,target,start,adjust_mask):
    if n*2 > target:

        adjust = adjust_mask % n
        if adjust > 0 and ((target - n) >= adjust):
            if b>a:
                b -= 1
            else:
                a-= 1

        if a < 0:
            a = 0
        if b < 0:
            b = 0

        return(a,b)

    if b % 2 == 1:
        return _solve(a//2,(b-1)//2,n*2, target, start, adjust_mask)
    else:
        return _solve((a-1)//2,b//2,n*2, target, start, adjust_mask)

def solve(n,k):
    a,b = _solve((n-1)//2,n//2,1,k,n,get_mask(n))
    return str(b)+" "+str(a)

def last_power_of_two(n):
    return 2**(n.bit_length()-1)

def get_mask(n):
    return n - last_power_of_two(n) + 1


T = int(input())
for t in range(T):
    n,k = [int(x) for x in input().split()]
    print("Case #{0}: {1}".format(t+1,solve(n,k)))
