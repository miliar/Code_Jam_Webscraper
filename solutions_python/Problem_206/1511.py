import sys
import math

def speeeedd(total_dist, other_horses):
    longest_time = 0
    for horse in other_horses:
        time = (total_dist - horse[0]) / horse[1]
        if time > longest_time:
            longest_time = time
    return round(total_dist/longest_time,6)

def read_in():

    tests = sys.stdin.readline()
    counts = int(tests.rstrip())
    for each in range(1,counts + 1):
        line = sys.stdin.readline().rstrip().split()
        total_dist = int(line[0])
        num_horses = int(line[1])
        other_horses = []
        for every in range(0,num_horses):
            liners = sys.stdin.readline().rstrip().split()
            other_horses.append((int(liners[0]), int(liners[1])))
        first = speeeedd(total_dist, other_horses)
        print('Case #' + str(each) + ':', first)


def main():
    lines = read_in()
if __name__ == '__main__':
    main()