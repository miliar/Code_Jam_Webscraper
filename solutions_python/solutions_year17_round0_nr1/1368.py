def flip(s, leftmost, k):
    for i in range(leftmost, leftmost + k):
        s[i] = (s[i] + 1) % 2
    return s

def solution(inputs):
        s, k = inputs.split()
        s, k = [1 if c == "-" else 0 for c in s], int(k)
        flips = 0
        leftmost = 0
        while sum(s):
            if leftmost + k > len(s):
                return "IMPOSSIBLE"
            if s[leftmost]:
                s = flip(s, leftmost, k)
                flips += 1
            leftmost += 1
        return flips

filename = input()
f = open(filename + ".in")
o = open(filename + ".out", "w")
t = int(f.readline())
for case in range(t):
    o.write("Case #{}: {}\n".format(case + 1, solution(f.readline())))