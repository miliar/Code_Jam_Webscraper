import sys
import heapq

def process_case(input, case):
    N, K = input.split(" ")
    K = int(K)
    N = int(N)
    h = [-N]
    spaces = {N: 1}
    mins, maxs = -1, -1

    while K > 0:
        largest_space = -heapq.heappop(h)
        num_spaces = spaces[largest_space]
        del spaces[largest_space]

        if largest_space % 2 == 0:
            mins = largest_space // 2 - 1
            maxs = largest_space // 2
        else:
            mins = maxs = largest_space // 2

        if mins not in spaces:
            spaces[mins] = 0
            heapq.heappush(h, -mins)
        spaces[mins] += num_spaces

        if maxs not in spaces:
            spaces[maxs] = 0
            heapq.heappush(h, -maxs)
        spaces[maxs] += num_spaces

        K -= num_spaces

    return "Case #" + str(case) + ": " + str(maxs) + " " + str(mins) + "\n"


def pancake(input, output):
    # Read input
    with open(output, "w") as o:
        with open(input, "r") as f:
            f.readline() # Read number of examples
            # Process examples
            i = 1
            for line in f:
                o.write(process_case(line, i))
                i += 1


if __name__ == '__main__':
    pancake(sys.argv[1], sys.argv[2])
