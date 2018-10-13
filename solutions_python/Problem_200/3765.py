
def ans(ls_n):
    if ls_n[0] == 0:
        return ans(ls_n[1:])
    n2 = ls_n[::-1]
    for i in range(len(n2)-1):
        if int(n2[i]) < int(n2[i+1]):
            n2[i+1] = str((int(n2[i+1])-1)%10)
            return ans(n2[i+1::][::-1]) + ['9']*(i+1)
    return n2[::-1]

with open('B-large.in', 'r') as f:
    with open('q2solution.txt', 'w') as solution:
        t = int(f.readline())
        for case in range(t):
            n = f.readline().strip()
            sol = int(''.join(ans(list(n))))
            solution.write('Case #' + str(case+1) + ': ' + str(sol) + '\n')
