import os


def is_tidy(x):
    l_x = list(str(x))
    return l_x == sorted(l_x)


if __name__ == '__main__':
    input_path = os.path.join(os.getcwd(), 'B-large.in')
    output_path = os.path.join(os.getcwd(), 'B-large.out')

    with open(input_path, 'r') as f_in:
        t = int(f_in.readline())
        cache = {}

        with open(output_path, 'w') as f_out:
            for x in range(1, t + 1):
                n = int(f_in.readline())
                i = 1
                while not is_tidy(n):
                    n -= 10 ** i
                    n = int(str(n)[:-i] + '9' * i)
                    i += 1

                f_out.write('Case #{x}: {y}'.format(x=x, y=n))
                f_out.write('\n')

        print('Finished')
