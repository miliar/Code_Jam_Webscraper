
def main():

    file_name = "B-small.out"
    # file_name = ".out"
    # file_name = ".out"

    try:

        # Open output file
        output_file = open(file_name, "w")

        # Read input data
        test_no = int(raw_input())

        for it_t in range(test_no):

            number = raw_input()

            if len(number) == 1:
                number_new = number

            else:
                temp = None
                for i in range(len(number) - 1):
                    if int(number[i]) > int(number[i + 1]):
                        temp = i
                        break

                print("Test case #" + str(it_t + 1) + " temp: " + str(temp))

                if temp is None:
                    number_new = number

                else:
                    if number[temp] == '1':
                        number_new = (len(number) - 1) * '9'

                    else:
                        number_new = ""
                        it = temp
                        while it >= 0:
                            tmp = int(number[it]) - 1
                            number_new = str(tmp) + number_new

                            if it == 0 or int(number[it - 1]) <= tmp:
                                break

                            it -= 1

                        number_new = number[0:it] + number_new
                        number_new += (len(number) - it - 1) * '9'

            if len(number_new) > len(number):
                number_new = number_new[-len(number):]

            # output_file.write("Case #" + str(it_t + 1) + ": " + number + " --> " + number_new)
            output_file.write("Case #" + str(it_t + 1) + ": " + number_new)
            if it_t != test_no - 1:
                output_file.write("\n")

        # Close output file
        output_file.close()

    except IOError:
        print("Cannot open file " + str(file_name))


if __name__ == "__main__":

    main()
