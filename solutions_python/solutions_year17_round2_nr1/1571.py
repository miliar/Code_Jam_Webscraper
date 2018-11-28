def main():
    output_file = open("/home/koofu/PycharmProjects/CodeJam_2017/Round 1B/Aout.out", 'w')

    with open("/home/koofu/PycharmProjects/CodeJam_2017/Round 1B/A-large.in", 'r') as f:
        test_cases = int(f.readline().strip())
        input_file = f.read().strip().splitlines()
        count = 0
        # print(test_cases)
        for x in range(test_cases):
            # print(x)
            answers = []
            holder = input_file[count].split()
            total_distance = float(holder[0])
            horses = int(holder[1])
            # print(horses)
            for y in range(horses):
                # print(y)
                count += 1
                value_holder = input_file[count].split()
                # print(value_holder)
                answers.append(float(float(total_distance-float(value_holder[0]))/float(value_holder[1])))
            count+=1
            # print(answers)
            output_file.write("Case #{0}: {1:.6f}\n".format(x+1, (total_distance/(max(answers)))))
            # output_file.write("Case #{0}: {1}".format(x, total_distance/max(answers[x])))


        # print(input_file)








            # output_file.write("Case #{0}: {1}".format(counter + 1, solve(line, f) + '\n'))


# def solve(stripped_line, in_file):
#     split_line = stripped_line.split()
    # for count in range(int(split_line[1])):


        # return "{0} {1}".format(queue[-2], queue[-1])


if __name__ == "__main__":
    main()
