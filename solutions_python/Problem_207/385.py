def run():
    N, R, O, Y, G, B, V = [int(x) for x in input().strip().split()]

    assert O == 0 and G == 0 and V == 0

    choices = [[R, 'R'], [B, 'B'], [Y, 'Y']]
    choices.sort(reverse=True)

    if choices[0][0] > choices[1][0] + choices[2][0]:
        return 'IMPOSSIBLE'

    avoid = ''
    first = None

    def get_char():
        nonlocal avoid, first
        choices.sort(key=lambda a: [a[0], a[1] == first], reverse=True)
        for choice in choices:
            left, color = choice
            if color != avoid:
                avoid = color
                if not first:
                    first = color
                choice[0] -= 1
                return color

    ans = ''
    for i in range(R+B+Y):
        ans += get_char()

    return ans

for case in range(int(input())):
    print("Case #{}: {}".format(case+1, run()))
