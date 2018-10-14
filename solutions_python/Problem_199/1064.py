def generic_function(n, k):
    n = [x for x in n]
    flips = 0
    while True:
        loc = -1
        for p in range(len(n)):
            if n[p] == '-':
                loc = p
                break
        if loc == -1:
            return flips
        elif loc + k > len(n):
            return 'IMPOSSIBLE'
        else:
            flips += 1
            for i in range(k):
                n[loc + i] = flip(n[loc + i])
        
    
def flip(p):
    if p == '-':
        return '+'
    else:
        return '-'
    
value = int(input())  # read a line with a single integer
for i in range(1, value + 1):
    n = input().split(' ')
    out = generic_function(n[0], int(n[1]))
    print("Case #{}: {}".format(i, out))

    