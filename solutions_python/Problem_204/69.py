import math

t = int(raw_input())

for case in xrange(1, t+1):
    num_ingredients, num_packages = map(int, raw_input().split())
    req = map(int, raw_input().split())
    ingredients = []  # ingredient -> [packages]
    for _ in xrange(num_ingredients):
        ingredients.append(map(int, raw_input().split()))

    ingredients = [sorted(ing) for ing in ingredients]

    largest_closest = 0
    for i, ing in enumerate(ingredients):
        res = []
        for i2 in ing:
            # closest = int(round(i2 / float(req[i])))
            # diff = abs(closest * req[i] - i2)
            # print 'diff', diff
            possible = []

            lowest = math.ceil(i2 / 1.1)
            highest = math.floor(i2 / 0.9)

            # print lowest, highest

            lowest = int(math.ceil(float(lowest) / req[i]))
            highest = int(math.floor(float(highest) / req[i]))

            # print lowest, highest

            if lowest <= highest:
                largest_closest = max(largest_closest, highest)
                res.append(range(lowest, highest+1))

            # if diff * 10 <= (req[i] * closest) and closest >= 1:
                # possible.append(closest)
                # largest_closest = max(largest_closest, closest)
                #
                # less = closest - 1
                # while True:
                #     diff = abs(less * req[i] - i2)
                #     if diff * 10 <= (req[i] * less) and less >= 1:
                #         possible.append(less)
                #         largest_closest = max(largest_closest, less)
                #         less -= 1
                #     else:
                #         break
                #
                # more = closest + 1
                # while True:
                #     diff = abs(more * req[i] - i2)
                #     if diff * 10 <= (req[i] * more) and more >= 1:
                #         possible.append(more)
                #         largest_closest = max(largest_closest, more)
                #         more += 1
                #     else:
                #         break

            # if possible:
            #     res.append(sorted(possible))
        ingredients[i] = res

    # print 'ingredients', ingredients

    servings = 1
    result = 0
    while servings <= largest_closest:
        ok = True
        for i, ing in enumerate(ingredients):
            while ing and ing[0][-1] < servings:
                # print 'pop', ing
                ing.pop(0)

            if not ing:
                # print 'done', i
                ok = False
                break

            if servings not in ing[0]:
                # print 'large', ing
                ok = False
                servings = ing[0][0]
                break

        if ok:
            for i, ing in enumerate(ingredients):
                ing.pop(0)

            result += 1
        else:
            if any(not ing for ing in ingredients):
                break

    print("Case #{}: {}".format(case, result))
