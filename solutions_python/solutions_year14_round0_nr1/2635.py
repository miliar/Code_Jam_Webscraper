__author__ = 'alexs'

if __name__ == '__main__':
    out = open("/Users/alexs/algorithmstraining/codejam2014/magic_trick/out.dat", "w")
    with open("/Users/alexs/algorithmstraining/codejam2014/magic_trick/A-small-attempt0.in") as f:
        nr_of_test_cases = int(f.readline().strip())
        for i in range(0, nr_of_test_cases):
            # read the first answer
            fa = int(f.readline()) - 1
            matrix = []
            for x in range(0, 4): matrix.append([int(p.strip()) for p in f.readline().split()])
            # print "matrix1:" + str(matrix)

            probable_numbers = [p for p in matrix[fa]]

            # read the second answer
            sa = int(f.readline()) - 1
            matrix2 = []
            for x in range(0, 4): matrix2.append([int(p.strip()) for p in f.readline().split()])
            # print "matrix2:" + str(matrix2)

            counter = 0
            number = None
            for p in matrix2[sa]:
                if p in probable_numbers:
                    number = p
                    counter += 1

            if counter > 1:
                print "Case #{test_case_number}: Bad magician!".format(test_case_number=str(i + 1))
                out.write("Case #{test_case_number}: Bad magician!\n".format(test_case_number=str(i + 1)))
            elif counter == 0:
                print "Case #{test_case_number}: Volunteer cheated!".format(test_case_number=str(i + 1))
                out.write("Case #{test_case_number}: Volunteer cheated!\n".format(test_case_number=str(i + 1)))
            else:
                print "Case #{test_case_number}: {val}".format(test_case_number=str(i + 1), val=str(number))
                out.write("Case #{test_case_number}: {val}\n".format(test_case_number=str(i + 1), val=str(number)))

    out.close()