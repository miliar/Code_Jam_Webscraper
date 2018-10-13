import math

# pancakes.append([r,h, side_area, 0])

def solve(n, k, pancakes):
    #print("n, k, pancakes:", n, k, pancakes)
    pancakes.sort(reverse=True, key=lambda x:x[0])
    #print(pancakes)

    for i in range(1, n):
        # set contributions
        pancakes[i][3] = (pancakes[i][1] * 2 * math.pi * pancakes[i][0])

    to_remove = n - k

    for i in range(to_remove):

        # set biggest pancake's contribution
        if len(pancakes) >= 2:
            top0 = ((pancakes[0][0]) ** 2) * math.pi
            top1 = ((pancakes[1][0]) ** 2) * math.pi
            diff = top0 - top1
            side0 = pancakes[0][1] * 2 * math.pi * pancakes[0][0]
            pancakes[0][3] = diff + side0

        index = 0
        min_contrib = float('inf')
        for i in range(len(pancakes)):
            if pancakes[i][3] < min_contrib:
                index = i
                min_contrib = pancakes[i][3]

        pancakes.pop(index)

    if len(pancakes) >= 2:
        top0 = ((pancakes[0][0]) ** 2) * math.pi
        #top1 = ((pancakes[1][0]) ** 2) * math.pi
        #diff = top0 - top1
        side0 = pancakes[0][1] * 2 * math.pi * pancakes[0][0]
        pancakes[0][3] = top0 + side0
    else:
        pancakes[0][3] = (pancakes[0][1] * 2 * math.pi * pancakes[0][0]) + (pancakes[0][0]**2 * math.pi)

    answer = sum([pancakes[i][3] for i in range(len(pancakes))])
    return answer


def main():
    #prefix = 'A-test'
    #prefix = 'A-small-attempt0'
    #prefix = 'A-small-attempt1'
    prefix = 'A-large'

    infile = open(prefix + '.in')
    outfile = open(prefix + '.out', 'w')

    cases = int(infile.readline().strip())
    for i in range(1, cases + 1):

        outfile.write("Case #{}: ".format(i))

        # read in details
        n, k = [int(i) for i in infile.readline().split()]
        pancakes = []
        for i in range(n):
            r, h = [int(i) for i in infile.readline().split()]
            side_area = 2 * r * h * math.pi
            pancakes.append([r,h, side_area, 0])
        ans = solve(n, k, pancakes)

        outfile.write(str(ans))
        outfile.write('\n')

    infile.close()
    outfile.close()

if __name__ == "__main__":
    main()