digits = ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")
from collections import Counter

def search(i, ans):
    global counter, good
    if i == 10:
        return
    if not counter:
        print('Case #%d:' % (case+1), ''.join(map(str, ans)))
        return
    cc = Counter(digits[i])
    if all(counter[c] >= cc[c] for c in digits[i]):
        counter -= cc
        ans.append(i)
        search(i, ans)
        ans.pop()
        counter += cc
    search(i+1, ans)


for case in range(int(input())):
    MSG = input()
    counter = Counter(MSG)
    good = []
    search(0, [])
