ans = []
with open('input.txt') as f:
    t = int(f.readline())
    for tst in range(t):
        a = int(f.readline())
        for i in range(a - 1):
            f.readline()
        x = set(map(int, f.readline().split()))
        for i in range(a, 4):
            f.readline()
        b = int(f.readline())
        for i in range(b - 1):
            f.readline()
        y = set(map(int, f.readline().split()))
        for i in range(b, 4): 
            f.readline()
        z = x.intersection(y)
        if len(z) == 0:
            result = 'Volunteer cheated!'
        elif len(z) == 1:
            result = str(next(iter(z)))
        else:
            result = 'Bad magician!'
        ans.append(result)
with open('output.txt', 'w') as f:
    for i in range(len(ans)):
        print('Case #{}:'.format(i + 1), ans[i], file=f)