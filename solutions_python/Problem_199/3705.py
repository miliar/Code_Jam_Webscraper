def get_flipped_part(pancakes):
    i = 0
    while (i < len(pancakes) and pancakes[i] == '+'):
        i += 1
    return pancakes[i:]


def flip(pancakes, number_of_flip):
    new_cakes = ''
    for i in range(number_of_flip):
        if (pancakes[i] == '+'):
            new_cakes += '-'
        else:
            new_cakes += '+'
    new_cakes += pancakes[number_of_flip:]
    return new_cakes


def pancake_flipper(pancakes, number_of_flip):
    count = 0
    flipped_cakes = pancakes

    while flipped_cakes and len(flipped_cakes) >= number_of_flip:
        flipped_cakes = get_flipped_part(flipped_cakes)

        if len(flipped_cakes) >= number_of_flip:
            count += 1
            flipped_cakes = flip(flipped_cakes, number_of_flip)

    if not flipped_cakes:
        return count
    else:
        return "Impossible"


output = open('output.in', 'w')
t = int(input())
for i in range(1, t + 1):
    n, m = [s for s in input().split(" ")]

    result = pancake_flipper(n, int(m))
    print("Case #{}: {}".format(i, result))
    output.write("Case #{}: {}\n".format(i, result))
