input = open('B-large.in', 'r')
output = open('B-large.out', 'w')
N = int(input.readline())
for case in range(1, N + 1):
    print("Case #", case, sep = "", end = ": ", file = output)
    n = list(input.readline().rstrip())
    i = 0
    while i < len(n) - 1 and n[i] <= n[i+1]:
        i += 1
    if i < len(n) - 1:
        n[i+1:] = ['9'] * (len(n) - i - 1)
        n[i] = str(int(n[i]) - 1)
        while i > 0 and n[i] < n[i-1]:
            n[i] = '9'
            n[i-1] = str(int(n[i-1]) - 1)
            i -= 1
    if n[0] == '0':
        n.pop(0)
    print("".join(n), file = output)
input.close()
output.close()