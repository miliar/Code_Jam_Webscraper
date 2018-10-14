def main():
    def flip(pancakes, k, start):
        if start < 0 or start + k > len(pancakes):
            raise IndexError
        else:
            output = [pancakes[start:start+k].translate(table)]
            output = [pancakes[:start]] + output + [pancakes[start+k:]]
            return ''.join(output)

    table = str.maketrans('+-', '-+')
    num_cases = int(input())
    solutions = {}
    output_string = 'Case #{}: {}'

    for line in range(1, num_cases + 1):
        closed = {}
        pancakes, k = input().split()
        k = int(k)
        closed['+' * len(pancakes)] = 0
        opens = closed.copy()

        while opens != {}:
            current = {}
            while opens != {}:
                stack, number = opens.popitem()
                for i in range(len(pancakes) - k + 1):
                    new_stack = flip(stack, k, i)
                    if new_stack not in closed:
                        closed[new_stack] = number + 1
                        current[new_stack] = number + 1
            opens = current

        if pancakes in closed:
            print(output_string.format(line, closed[pancakes]))
        else:
            print(output_string.format(line, 'IMPOSSIBLE'))


if __name__ == '__main__':
    main()
