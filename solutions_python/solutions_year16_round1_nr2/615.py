
def main():
    of = open('rankfile-large.out', 'w', 1)

    with open('B-large.in', 'r') as f:
        count = int(f.readline().rstrip('\n'))
        for i in range(count):
            number = int(f.readline().rstrip('\n'))
            matrix_dic = {}

            output = []
            for c in range(number*2 - 1):
                row = f.readline().rstrip('\n')

                for j in row.split(' '):
                    value = int(j)
                    if value in matrix_dic:
                        matrix_dic[value] += 1
                    else:
                        matrix_dic[value] = 1

            for k in matrix_dic:
                if matrix_dic[k]&1:
                    output.append(k)

            output.sort()

            of.write('Case #{}:'.format(i + 1))
            for o in output:
                 of.write(' {}'.format(o))
            of.write('\n')


    of.close()

if __name__ == "__main__":
    main()
