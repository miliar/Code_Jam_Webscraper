__author__ = 'avital'


def is_tidy(num):
    return "".join(sorted(str(num))) == str(num)

def main():
    with open('small.in', 'r') as small_input:
        with open('small_solution.txt', 'w') as small_output:
            cases = int(small_input.readline())
            for case in range(1, cases+1):
                for num in range(0, int(small_input.readline()) + 1):
                    if is_tidy(num):
                        max_tidy = num
                small_output.write("Case #{case}: {max_tidy}\n".format(case=case, max_tidy=max_tidy))



if __name__ == '__main__':
    main()