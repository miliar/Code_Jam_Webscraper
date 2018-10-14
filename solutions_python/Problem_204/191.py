def inp():
    t = int(input())
    cases = []
    for i in range(t):
        n, p = tuple(int(x) for x in input().split())
        recipe = tuple(int(x) for x in input().split())
        q = []
        for j in range(n):
            q.append([int(x) for x in input().split()])
        cases.append((n, p, recipe, q))
    return cases


def servings(recipe, amount):
    lower = amount / (recipe * 1.1)
    lower = int(lower) + (0 if lower.is_integer() else 1)
    upper = int(amount / (recipe * .9))
    return lower, upper


def process(n, p, recipe, q):
    for packages in q:
        packages.sort()

    count = 0
    picked = [-1] * n
    for i, q0 in enumerate(q[0]):
        # print("i = {}, q0 = {}".format(i, q0))
        lower, upper = servings(recipe[0], q0)
        # print("lower = {}, upper = {}".format(lower, upper))
        done = False
        if lower <= upper:
            done = True
            for ingr in range(1, n):
                # print("{}th ingredient".format(ingr + 1))
                for j, package in enumerate(q[ingr][picked[ingr] + 1:]):
                    # print("package {}".format(j + 1))
                    if package > upper * recipe[ingr] * 1.1:
                        done = False
                        break
                    elif package >= lower * recipe[ingr] * .9:
                        # print("got picked")
                        picked[ingr] += j
                        break
                    elif picked[ingr] + j + 2 == p:
                        done = False

        if done:
            count += 1

    return count


def main():
    cases = inp()
    for i, case in enumerate(cases):
        # print(case)
        print("Case #{}: {}".format(i + 1, process(*case)))


main()
