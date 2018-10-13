import sys

def best_possible(total):
    for i in range(10, -1, -1):
        if i == 0:
            sum_list = [0]
        else:
            sum_list = [
                i * 3, 
                (i * 2) + (i - 1),
                i + ((i - 1) * 2)
            ]

        if total in sum_list:
            return i

def best_suprising(total):
    for i in range(10, -1, -1):
        if i == 0:
            sum_list = [0]
        elif i == 1:
            sum_list = [1]
        else:
            sum_list = [
                i * 3, 
                (i * 2) + (i - 1),
                (i * 2) + (i - 2),
                i + ((i - 1) * 2),
                i + (i - 1) + (i - 2),
                i + ((i - 2) * 2)
            ]

        if total in sum_list:
            return i

def main():
    file_name = sys.argv[1]
    input_file = open(file_name, "r").readlines()
    test_cases = int(input_file[0])

    for i in range(1, test_cases + 1):
        test_numbers = input_file[i].strip().split(" ")
        num_googlers = int(test_numbers[0])
        num_suprising = int(test_numbers[1])
        best_result = int(test_numbers[2])
        points_list = [int(points) for points in test_numbers[3:]]

        pass_num = 0
        for total in points_list:
            if best_possible(total) >= best_result:
                pass_num += 1
            elif num_suprising and (best_suprising(total) >= best_result):
                pass_num += 1
                num_suprising -= 1

        print "Case #%s: %s" % (i, pass_num)

if __name__ == "__main__":
    main()
