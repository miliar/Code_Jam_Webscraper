from heapq import heappush, heappop

def solve(n, k):
    area = []
    heappush(area, -n)
    while k > 0:
        max_area = -heappop(area)
        if max_area % 2 == 0:
            max_empty = max_area / 2
            min_empty = max_empty - 1
        else:
            max_empty = min_empty = (max_area - 1) / 2
        heappush(area, -max_empty)
        heappush(area, -min_empty)
        k -= 1

    return "%d %d" % (max_empty, min_empty)


def main():
    input_file_name = 'C-input.in'
    output_file_name = 'C-output.out'
    with open(input_file_name) as fin:
        with open(output_file_name, 'w') as fout:
            t = int(fin.readline())
            for i in range(t):
                n, k = tuple(map(int, fin.readline().split()))
                fout.write("Case #%d: %s\n" % (i+1, solve(n, k)))

main()