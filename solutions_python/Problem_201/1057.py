import argparse
import heapq
from fractions import gcd

# interestingly, there's no max heap implementation in python.

def get_min_max(num_stalls, people):
    if num_stalls == people:
        return "0 0"
    #decrease = gcd(num_stalls, people)
    #num_stalls/=decrease
    #people/=decrease
    open_spaces = []
    spaces = (0,0)
    heapq.heappush(open_spaces, num_stalls*-1)
    while people >= 1:
        max_space = heapq.heappop(open_spaces) * -1 - 1  # space minus where the person is sitting
        spaces = (max_space // 2, max_space - max_space // 2)
        heapq.heappush(open_spaces, spaces[0]*-1)
        heapq.heappush(open_spaces, spaces[1]*-1)
        people-=1
    return "{} {}".format(max(spaces), min(spaces))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", dest="output_file", help="output file")
    args = parser.parse_args()

    with open(args.output_file) as f, open(args.output_file.replace("in.txt", "out.txt"), "w") as out:
        test_cases = int(f.readline().strip())
        for i, _ in enumerate(range(test_cases)):
            stalls, people = [int(n) for n in f.readline().strip().split()]
            result = get_min_max(stalls, people)
            #print(result)
            out.write("Case #{}: {}\n".format(i+1, result))


if __name__ == "__main__":
    main()
