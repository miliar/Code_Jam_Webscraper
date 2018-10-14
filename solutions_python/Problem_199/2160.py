def solve(pancakes, k):
    n = 0

    # find a pancake (-)
    for i in range(len(pancakes)):
        if pancakes[i] == '-':
            if i + k > len(pancakes):
                return None
            new_block = ''.join(['-' if c == '+' else '+' for p in pancakes[i:i+k] for c in p])
            pancakes = pancakes[:i] + new_block + pancakes[i+k:]
            n += 1

    return n

num_cases = int(input())

for i in range(num_cases):
    pancakes, k = input().split(' ')
    k = int(k)

    n = solve(pancakes, k)

    print("Case #%d: %s" % (i+1, n if n is not None else 'IMPOSSIBLE'))
