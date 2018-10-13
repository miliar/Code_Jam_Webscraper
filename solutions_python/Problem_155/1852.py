__author__ = 'Haewon'


# do the job
def main_job(s_max, counts):
    curr_count = 0
    result = 0
    for i in range(s_max+1):
        add_count = 0
        if counts[i] > 0:
            if curr_count >= i:
                curr_count += counts[i]
            else:
                add_count = i - curr_count
                curr_count += add_count
                curr_count += counts[i]
                result += add_count
        # print("%d: add_count = %d curr_count = %d" %(i, add_count, curr_count))

    return result


def main():
    #input read
    input_file = open("input4.in", 'rt')
    num_cases = int(input_file.readline())

    #output write
    output_file = open("output4.txt", 'w')

    for i in range(num_cases):
        line = input_file.readline()
        line = line.split()
        s_max = int(line[0])
        counts = []
        for j in range(s_max+1):
            counts.append(int(line[1][j]))

        result = main_job(s_max, counts)
        #
        # if result >= 0 :
        #     output = "Case #%d: %d\n" %(i+1, result)
        # else:
        #     output = "Case #%d: impossible\n" %(i+1)

        output = "Case #%d: %d\n" %(i+1, result)
        output_file.write(output)
        print(i+1)
    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()