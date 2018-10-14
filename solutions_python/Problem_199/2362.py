cases = int(input())
results = []
for c in range(cases):
    pancakes, k = input().split(" ")
    k = int(k)

    data = [True if p=="+" else False for p in pancakes]
    tries = 0
    while False in data:
        ipos = data.index(False)
        if len(data) - ipos < k:
            tries = "IMPOSSIBLE"
            break
        tries += 1
        for n in range(k):
            data[ipos+n] = not data[ipos+n]
    results.append(tries)

for i, r in enumerate(results):
    print("Case #{}: {}".format(i+1, r))
