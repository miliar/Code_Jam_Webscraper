
import time


def main():

    # file_name = "example.out"
    # file_name = "C-small.out"
    file_name = "C-medium.out"
    # file_name = "C-large.out"

    try:

        # Open output file
        output_file = open(file_name, "w")

        # Read input data

        test_no = int(raw_input())

        start = time.time()

        it_t = 0

        while it_t < test_no:

            end = time.time()

            print("Iteration: " + str(it_t) + ", time:  " + str(end - start) + "\n")

            line = raw_input().split(" ")
            n = int(line[0])
            k = int(line[1])

            if k == 1:
                y, z = make_pair(n)

            # elif n % 2 == 0 and k > n / 2:
            #
            #     print("n: " + str(n) + ", n/2 : " + str(n / 2) + ", k: " + str(k))
                # y = 0
                # z = 0
            #
            # elif n % 2 == 1 and k > (n + 1) / 2:
            #     y = 0
            #     z = 0

            else:

                right, left = make_pair(n)
                i = 1
                curr_set = [(right, left)]
                # print("N: " + str(n) + ", K: " + str(k))
                # print("Current set - init: " + str(curr_set))

                while True:

                    # print("Current set while: " + str(curr_set))

                    prev_length = len(curr_set)
                    # print("Previous length: " + str(prev_length))
                    temp_set = []
                    # print("Temp set: " + str(temp_set))
                    it_set = 0
                    len_set = len(curr_set)
                    while it_set < len_set:

                        r, l = make_pair(curr_set[it_set][0])
                        # print("Item 0 - R: " + str(r) + ", L: " + str(l))
                        temp_set.append((r, l))
                        r, l = make_pair(curr_set[it_set][1])
                        # print("Item 1 - R: " + str(r) + ", L: " + str(l))
                        temp_set.append((r, l))

                        it_set += 1

                    # print("Temp set before sort: " + str(temp_set))
                    temp_set.sort(key=lambda e: (-e[0], -e[1]))
                    # print("Temp set after sort: " + str(temp_set))
                    i += len(temp_set)

                    if i >= k:
                        # print("K: " + str(k) + ", PL: " + str(prev_length))
                        index = k - (i - len(temp_set)) - 1
                        # print("index: " + str(index))
                        y = temp_set[index][0]
                        z = temp_set[index][1]
                        break

                    curr_set = temp_set

            output_file.write("Case #" + str(it_t + 1) + ": " + str(y) + " " + str(z))
            # output_file.write("Case #" + str(it_t + 1) + ": " + str(n) + "," + str(k) +
            #                   " --> " + str(y) + " " + str(z))
            if it_t != test_no - 1:
                output_file.write("\n")

            start = time.time()

            it_t += 1

        # Close output file
        output_file.close()

    except IOError:
        print("Cannot open file " + str(file_name))


def make_pair(n):

    right = n / 2
    if n % 2 == 0:
        left = right - 1
    else:
        left = right

    return right, left


if __name__ == "__main__":

    s = time.time()
    main()
    e = time.time()

    print("Time: " + str(e - s))
