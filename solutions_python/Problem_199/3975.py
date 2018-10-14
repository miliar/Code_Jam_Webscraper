from heapq import heappop, heappush


def convert_to_int(pancakes):
    total = 0
    for index, v in enumerate(reversed(pancakes)):
        if v == '+':
            total += 2**index

    return total


def convert_from_int(i, int_width):
    digits  = bin(i)[2:]
    symbols = [('+' if x == '1' else '-') for x in digits]

    if len(symbols) < int_width:
        symbols = ['-' for x in range(int_width - len(symbols))] + symbols

    return ''.join(symbols)


def neighbors(n, spatula_width, int_width):
    xors = [((2**spatula_width - 1) << x)
            for x in range(int_width - spatula_width + 1)]

    return [n ^ xor for xor in xors]


# solves uses shortest path (priortiy queue) and converts to ints for faster neighbors.
def solve(start, end, spatula_width, int_width):
    seen  = set()
    queue = [(0, start)]

    while len(queue) > 0:
        moves, value = heappop(queue)

        if value == end:
            return moves

        seen.add(value)

        for n in neighbors(value, spatula_width, int_width):
            if n not in seen:
                heappush(queue, (moves + 1, n))

    return "IMPOSSIBLE"


num_tests = int(input())
for i in range(1, num_tests + 1):
    test_parts    = input().split(" ")
    pancakes      = test_parts[0]
    spatula_width = int(test_parts[1])

    start_int = 2 ** len(pancakes) - 1
    end_int   = convert_to_int(pancakes)

    result = solve(start_int, end_int, spatula_width, len(pancakes))

    print("Case #{}: {}".format(i, result))
