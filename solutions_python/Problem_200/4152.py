with open('in', 'r') as f:
    T = int(f.readline())
    testcases = map(int, f.readlines())

def is_sorted(i):
    i = [int(w) for w in str(i)]
    for j in range(len(i)-1):
        if i[j] > i[j+1]: return False
    return True

for t,n in enumerate(testcases):
    res = n
    while not is_sorted(res): res -= 1
    print('Case #{}: {}'.format(t+1, res))
