
BLANK = '-'
SUNNY = '+'

# Pure
def flip(c):
    return ('+' if c == '-' else (
        '-' if c == '+' else c))

# Mutates stuff
def flip_from(cakes, start, width):
    for i in range(start, start + width):
        cakes[i] = flip(cakes[i])

def solve(cakes, width):
    steps = 0
    for _ in range(len(cakes)):  # forever
        try:
            first_blank = cakes.index(BLANK)
        except ValueError:
            return steps
        if len(cakes) < first_blank + width:
            return 'IMPOSSIBLE'
        flip_from(cakes, first_blank, width)
        steps += 1

def main():
    t = int(input())
    for ti in range(1, t + 1):
        cakes, width = input().split()
        cakes = list(cakes)
        width = int(width)
        print("Case #{}: {}".format(ti, solve(cakes, width)))

if __name__ == '__main__':
    main()
