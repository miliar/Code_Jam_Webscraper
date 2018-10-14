import operator


for i in range(int(input())):

    n = int(input())
    ns = tuple(map(int, str.split(input())))
    deltas = tuple(map(operator.sub, ns, ns[1:]))
    f = sum(filter(lambda x: x > 0, deltas))
    c = max(deltas)
    s = 0
    for el in ns[:-1]:

        s += min(el, c)

    print(str.format("Case #{}: {} {}", i + 1, f, s))
