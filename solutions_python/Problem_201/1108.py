loops = range(1, int(input()) + 1)
for loop in loops:
    bathrooms, people = [int(i) for i in input().split()]
    if bathrooms < people:
        print("There are more people than bathrooms!")
        people = bathrooms
    empty = {bathrooms: 1}
    for i in range(people):
        chosen = max(empty.keys())
        empty[chosen] -= 1
        if empty[chosen] == 0:
            del empty[chosen]
        if chosen == 1:
            new_div = [0, 0]
        else:
            half = int(chosen/2)
            new_div = [half, half] if chosen % 2 != 0 else [half, half - 1]
            for new in new_div:
                try:
                    empty[new] += 1
                except KeyError:
                    empty[new] = 1
    print("Case #{}: {} {}".format(loop, new_div[0], new_div[1]))