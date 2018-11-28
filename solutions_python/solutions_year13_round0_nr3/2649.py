__author__ = 'mshafer'

from math import sqrt

def main():
    f = file("C-small-attempt0.in", "r")
    num_test_cases = int(f.readline())

    for i in range(num_test_cases):
        line = map(int, f.readline().strip().split())
        start = line[0]
        end = line[1]
        count = 0

        for j in range(start, end + 1):
            j_string = str(j)
            if j_string == j_string[::-1]:
                root = sqrt(j)
                if root % 1 == 0:
                    root = int(root)
                    root_string = str(root)
                    if root_string == root_string[::-1]:
                        count += 1

        print "Case #" + str(i + 1) + ": " + str(count)

if __name__ == "__main__":
    main()