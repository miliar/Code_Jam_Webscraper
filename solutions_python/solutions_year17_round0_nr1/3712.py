import sys

def flippan(s):
    for i in range(len(s)):
        s[i] = '+' if s[i] == '-' else '-'
    return s

def doflip(s, k, i):
    return s[:i] + flippan(s[i:i+k]) + s[(i+k):]

def f(cakes, k):
    head = 0
    num_flips = 0
    end = len(cakes) - k
    while head <= end:
        if cakes[head] == '+':
            head += 1
            continue
        cakes = doflip(cakes, k, head)
        num_flips += 1
        head += 1
    for x in cakes[end:]:
        if x != '+':
            return 'IMPOSSIBLE'
    return num_flips 

def main():
    i = 1
    for l in sys.stdin.readlines()[1:]:
        cakes, k = l.strip().split(" ")
        flips = f(list(cakes), int(k))
        print "Case #{}: {}".format(i, flips)
        i+=1

if __name__ == "__main__":
    main()
