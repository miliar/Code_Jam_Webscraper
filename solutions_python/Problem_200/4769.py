def is_tidy(n):
    res = str(n)
    last_num = int(res[0])
    for num in res:
        if int(num) < last_num:
            return False
        last_num = int(num)
    return True


def get_tidy_number(n):
    if n <= 0:
        return 0

    # num = [1]
    # for i in range(n - 1):
    #     #print(num)
    #     last_pos = len(num) - 1
    #     add_one(num, last_pos)

    while not is_tidy(n):
        n -= 1

    return n


if __name__ == "__main__":
    print("Test Starting")
    input_file = open("C:\\Users\\Yash\\Downloads\\input.txt")
    output_file = open("C:\\Users\\Yash\\Downloads\\output.txt", 'w')
    input_number = int(input_file.readline())
    for i in range(input_number):
        output = get_tidy_number(int(input_file.readline()))
        output_file.write("case #" + str(i + 1) + ": " + str(output) + "\n")

    input_file.close()
    output_file.close()
    print("FIN")