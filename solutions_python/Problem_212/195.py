import itertools

two = [(1,1)]
three = [(1,2),(1,1,1),(2,2,2)]
four = [(1,3),(2,2),(1,1,2),(2,3,3),(1,1,1,1),(3,3,3,3)]

combs = [[] for _ in range(5)]
combs[2] = two
combs[3] = three
combs[4] = four

ret = []
with open('A-large.in', 'r') as file:
    t = int(file.readline())
    for __ in range(t):
        n, p = map(int, file.readline().split())
        g = list(map(int, file.readline().split()))

        groups = {i:0 for i in range(p)}
        for i in range(n):
            groups[g[i]%p] += 1
        bundles = groups[0]
        # print(groups)
        for comb in combs[p]:
            while True:
                enough = True
                for i in comb:
                    groups[i] -= 1
                    if groups[i] < 0:
                        enough = False
                if not enough:
                    for i in comb:
                        groups[i] += 1
                    break
                else:
                    bundles += 1
            # print(__, groups, comb, bundles)
        if any(groups[i] for i in range(1, p)):
            bundles += 1


        ret.append(bundles)


with open('Aout_large.txt', 'w') as outfile:
    for i in range(t):
        outfile.write("Case #%d: %s\n" %(i+1, ret[i]))