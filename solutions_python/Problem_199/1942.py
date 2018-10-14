f = open('input.txt', 'r')
out = open('output.txt', 'w') 
n = int(f.readline())

def solve(pancakes, k):
    res = helper(0, pancakes, k)
    if res == -1:
        return "IMPOSSIBLE"
    return res

def helper(idx, pancakes, k):
    if idx > len(pancakes)-k:
        for i in xrange(idx, len(pancakes)):
            if pancakes[i] == '-':
                return -1
        return 0
    if pancakes[idx] == '-':
        for i in xrange(idx, idx+k):
            if pancakes[i] == '-':
                pancakes[i] = '+'
            else:
                pancakes[i] = '-'
        flipped = True
    else:
        flipped = False
        
    result = helper(idx+1, pancakes, k)
    if result == -1:
        return -1
    if flipped:
        for i in xrange(idx, idx+k):
            if pancakes[i] == '-':
                pancakes[i] = '+'
            else:
                pancakes[i] = '-'
        return 1+result
    else:
        return result

for i in xrange(n):
    [pancakes, k] = f.readline().split()
    ans = solve(list(pancakes), int(k))
    print("Case #%d: %s" % (i+1, ans))
    out.write("Case #%d: %s\n" % (i+1, ans))




    
