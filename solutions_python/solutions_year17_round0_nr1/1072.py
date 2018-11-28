for case in range(1, int(input()) + 1):
    cakes, k = input().strip().split(' ')
    cakes = [c == '+' for c in cakes]
    k = int(k)

    for i in range(len(cakes)):
        try:
            idx = cakes.index(False)
            try:
                for j in range(idx, idx + k):
                    cakes[j] = not cakes[j]
            except IndexError:
                flips = 'IMPOSSIBLE'
                break
        except ValueError:
            flips = i
            break

    else:
        flips = 'IMPOSSIBLE'

    print("Case #{}: {}".format(case, flips))
