from collections import Counter

N = int(input())
ans = []
for _ in range(N):
    pancakes, K = input().strip().split()
    K = int(K)
    count = Counter(pancakes)
    size = len(pancakes)
    # rule out cases first
    if count['-'] == 0 or not pancakes:
        ans.append(0)
        continue
    elif K > size:
        ans.append('IMPOSSIBLE')
        continue
    else:
        new_pan = list(pancakes)
        times = 0
        i = new_pan.index('-')
        while i <= size - K:
            for a in range(K):
                if new_pan[a+i] == '+':
                    new_pan[a+i] = '-'
                else:
                    new_pan[a+i] = '+'
            times += 1
            try:
                i = new_pan.index('-')
            except:
                break
        if '-' not in new_pan:
            ans.append(times)
        else:
            ans.append('IMPOSSIBLE')
print(ans)

f = open('output', 'w')
for i, a in enumerate(ans):
    f.write("Case #%i: %s" % ((i+1), str(a)))
    f.write('\n')
f.close
