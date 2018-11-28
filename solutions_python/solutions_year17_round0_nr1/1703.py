# Problem C


def solve(pancakes, flipper_size):
    pancake_list = list(pancakes)
    pancake_len = len(pancake_list)
    flip_count = 0

    for i in range(0, pancake_len - flipper_size + 1):
        pancake = pancake_list[i]
        if pancake == '-':
            flip_count += 1
            for j in range(flipper_size):
                pancake_flip = pancake_list[i + j]
                if pancake_flip == '+':
                    pancake_list[i + j] = '-'
                else:
                    pancake_list[i + j] = '+'

    for pancake in pancake_list:
        if pancake == '-':
            return False, 0

    return True, flip_count



def main():
    #inputFile = "A-small-attempt11.in"
    inputFile = "A-large.in"
    outFile = inputFile + ".out"

    inpf = open(inputFile, "r")
    outf = open(outFile, "w")

    testCase = int(inpf.readline())

    false_msg = "IMPOSSIBLE"

    for case in range(testCase):

        input = inpf.readline().split(' ')
        pancakes = input[0]
        flipper_size = int(input[1])
        rst, cnt = solve(pancakes, flipper_size)

        if rst:
            result = 'Case #{}: {}\n'.format(case + 1, cnt)
        else:
            result = 'Case #{}: {}\n'.format(case + 1, false_msg)

        print(result, end='')
        outf.write(result)
    inpf.close()
    outf.close()





if __name__ == "__main__":
    main()
