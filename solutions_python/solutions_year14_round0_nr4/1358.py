__author__ = 'nik'

def main():
    output_file = open('output', 'w')
    with open('input') as input_file:
        next(input_file)
        i = 0
        case_num = 0
        row1 = []
        row2 = []
        result = {}

        for line in input_file:
            if i == 0:
                i += 1
                continue
            if i == 1:
                row1 = line
                row1 = row1.split(' ')
                row1 = map(float, row1)
                row1.sort()
            if i == 2:
                row2 = line
                row2 = row2.split(' ')
                row2 = map(float, row2)
                row2.sort()
            i += 1
            if i == 3:
                i = 0
                first = 0
                last = len(row2) - 1
                for e in row1:
                    if e > row2[first]:
                        result[e] = row2[first]
                        first += 1
                    else:
                        result[e] = row2[last]
                        last -= 1
                res2 = 0
                for k, v in result.iteritems():
                    if k > v:
                        res2 += 1

                res1 = 0
                for e in row1:
                    suc = False
                    for k in row2:
                        if k > e:
                            row2.remove(k)
                            suc = True
                            break
                    if not suc:
                        res1 += 1
                        row2.remove(row2[0])

                case_num += 1
                output = "Case #%d: %d %d\n"%(case_num, res2, res1)
                print(output)
                output_file.write(output)

                row1 = []
                row2 = []
                result = {}

if __name__ == '__main__': main()