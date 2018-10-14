def solve():
    s = list(input())
    while list(sorted(s)) != s:
        for i in range(len(s)):
            if s[i] > s[i+1]:
                s[i] = chr(ord(s[i])-1)
                s = s[:i+1] + ['9'] * (len(s) - i - 1)
                break
    return ''.join(s).lstrip('0')

tt = int(input())

for i in range(1, tt+1):
    print("Case #%d:" % i, solve())

