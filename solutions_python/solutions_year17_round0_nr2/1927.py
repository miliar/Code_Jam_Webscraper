def is_tidy(number):
    number = list(str(number))

    for i in range(len(number) - 1):
        if number[i] > number[i + 1]:
            return False

    return True

def tidy_numbers(inputfile, outputfile):
    fin = open(inputfile, "r")
    fout = open(outputfile, "w")
    no_of_cases = int(fin.readline())

    case_no = 1

    while case_no <= no_of_cases:
        N = int(fin.readline().strip("\n"))
        N_str = str(N)

        i = 0
        while not is_tidy(N):
            N -= 10**i * (int(N_str[len(N_str) - i - 1]) + 1)
            i += 1
            N_str = str(N)

        fout.write("Case #" + str(case_no) + ": " + str(N) + "\n")

        case_no += 1


    fin.close()
    fout.close()

tidy_numbers("B-large.in", "B-large.out")