
def main():
    t = int(input())

    for case in range(t):
        pancakes, width = [s for s in input().strip().split()]
        pancakes = [c == '+' for c in pancakes]
        width = int(width)
        moves = 0

        for i in range(len(pancakes)-width+1):
            if not pancakes[i]:
                for p in range(width):
                    pancakes[i+p] = not pancakes[i+p]
                moves += 1

        if not all(pancakes[-width:]):
            moves = 'IMPOSSIBLE'

        print("Case #{0}: {1}".format(case+1, moves))


if __name__ == '__main__':
    main()
