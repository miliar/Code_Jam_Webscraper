def main():
    t = int(raw_input())
    for case in range(1, t + 1):
        nums = [int(_) for _ in raw_input().split()]
        del nums[0]
        T = 0
        for a in nums:
            for b in nums:
                if a > b:
                    if T == 1: break
                    T = gcd(T, a - b)
        res = 0
        for a in nums:
            res = max(res, (T - a % T) % T)
        print 'Case #%d: %d' % (case, res)

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

if __name__ == '__main__': main()
