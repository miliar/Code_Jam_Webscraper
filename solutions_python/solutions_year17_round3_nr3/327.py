import os

if __name__ == '__main__':
    input_path = os.path.join(os.getcwd(), 'C-small-1-attempt0.in')
    output_path = os.path.join(os.getcwd(), 'C-small-1-attempt0.out')

    with open(input_path, 'r') as f_in:
        t = int(f_in.readline())

        with open(output_path, 'w') as f_out:
            for x in range(1, t + 1):
                n, k = map(int, f_in.readline().split())
                u = float(f_in.readline())
                cores = [float(s) for s in f_in.readline().split()]

                if n == k:
                    cores.sort()

                    # найти минимальный уровень и кол-во cores на нем
                    # отнять от следующего уровня значение минимального уровня:
                    #   если u > него:
                    #       разделить разницу на кол-во cores в нижнем уровне
                    #   иначе:
                    #       разделить u на кол-во cores в нижнем уровне

                    while u > 0:
                        # найти минимальный уровень и кол-во cores на нем
                        i = 0

                        while i < k-1 and cores[i] == cores[i+1]:
                            i += 1

                        if i < k - 1:
                            diff = cores[i + 1] - cores[i]
                            if u >= diff * (i+1):
                                train = diff
                                for j in range(i+1):
                                    cores[j] += train
                                u -= diff * (i+1)
                            else:
                                train = u / (i + 1)
                                for j in range(i + 1):
                                    cores[j] += train
                                u = 0
                        else:
                            train = u / (i + 1)
                            for j in range(i + 1):
                                cores[j] += train
                            u = 0

                    result = cores[0]
                    for c in cores[1:]:
                        result *= c

                    f_out.write('Case #{x}: {y}'.format(x=x, y=result))
                    f_out.write('\n')

        print('Finished')
