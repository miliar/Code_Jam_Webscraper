# python A.py < A-small-attempt0.in > A-small-attempt0.out
# 
# list(raw_input()) # List of chars
# [int(n) for n in raw_input().split()] # List of ints

if __name__ == "__main__":
    testcases = input()
    
    
    def negate(x):
        if len(x) > 1: return x[1]
        return '-' + x
    
    def mul(x, y):
        if x == '1': return y
        elif y == '1': return x
        elif len(x) > 1: return negate(mul(negate(x), y))
        elif len(y) > 1: return negate(mul(x, negate(y)))
        elif x == 'i':
            if y == 'i': return '-1'
            elif y == 'j': return 'k'
            else: return '-j'
        elif x == 'j':
            if y == 'i': return '-k'
            elif y == 'j': return '-1'
            else: return 'i'
        else:
            if y == 'i': return 'j'
            elif y == 'j': return '-i'
            else: return '-1'
    
    for case in xrange(1, testcases+1):
        
        nums = [int(n) for n in raw_input().split()]
        repeat = list(raw_input())
        chars = []
        for _ in range(nums[1]):
            chars.extend(repeat)
        i, curr = 0, '1'
        while i < len(chars) and curr != 'i':
            curr = mul(curr, chars[i])
            i += 1
        if i != len(chars):
            k, curr = len(chars) - 1, '1'
            while k >= i and curr != 'k':
                curr = mul(chars[k], curr)
                k -= 1
            if k >= i:
                curr = '1'
                for j in range(i, k + 1):
                    curr = mul(curr, chars[j])
            else:
                curr = 'x'
        else:
            curr = 'x'
        
        print("Case #%i: %s" % (case, "YES" if curr == 'j' else "NO"))

