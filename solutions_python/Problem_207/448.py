def main():
    num_cases = int(input())
    for case_num in range(num_cases):
        params = input().split(' ')
        num_unicorns = int(params[0])
        colors = [int(p) for p in params[1:]]
        color_to_letter = {0: 'R', 1: 'O', 2: 'Y', 3: 'G', 4: 'B', 5: 'V'}

        possible_next = [(idx, colors[idx]) for idx in range(len(colors))]
        possible_next = sorted(possible_next, key=lambda x: x[1])
        first_color_idx = possible_next[0][0]
        for idx, color in possible_next:
            if color > 0:
                first_color_idx = idx
                break

        arrangement = [color_to_letter[first_color_idx]]
        prev_color_idx = first_color_idx
        colors[prev_color_idx] -= 1
        num_colors = len(colors)
        for unicorn_num in range(num_unicorns - 1):
            possible_next = []
            for i in range(4, 1, -1):
                idx = (prev_color_idx + i) % num_colors
                num = colors[idx]
                possible_next.append((idx, num))

            possible_next = list(reversed(
                sorted(possible_next, key=lambda x: x[1])))

            next_color_idx = possible_next[0][0]
            for idx, color in possible_next:
                if color > 0:
                    next_color_idx = idx
                    break

            if colors[next_color_idx] > 0:
                arrangement.append(color_to_letter[next_color_idx])
                colors[next_color_idx] -= 1
                prev_color_idx = next_color_idx
            else:
                arrangement = []
                break

        res = 'IMPOSSIBLE' if len(arrangement) == 0 else ''.join(arrangement)
        print('Case #{0}: {1}'.format(case_num + 1, res))


main()
