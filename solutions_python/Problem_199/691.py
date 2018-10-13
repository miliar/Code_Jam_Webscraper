
def flip(x):
    return '-' if x == '+' else '+'

def solve(s, k):
    seen = [s]
    count = 0
    for i in range(len(s)):
        if s[i] == '-':
            if (i + k > len(s)):
                return "IMPOSSIBLE"
            s = s[0:i] + [flip(x) for x in s[i:i + k]] + s[i + k:len(s)]
            count += 1
    return count

t = int(input())
for i in range(t):
    print("Case #" + str(i + 1) + ":", end=' ')
    s, k = input().split()
    print(solve(list(s), int(k)))