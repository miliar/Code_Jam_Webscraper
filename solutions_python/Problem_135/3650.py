def calculate(cards_arr1, cards_arr2, row1, row2):
    row1_arr = cards_arr1[row1 - 1]
    row2_arr = cards_arr2[row2 - 1]

    result = list(set(row1_arr) & set(row2_arr))
    if len(result) == 0:
        return 'Volunteer cheated!'
    elif len(result) > 1:
        return 'Bad magician!'
    else:
        return result[0]

if __name__ == '__main__':
    f = open('input.txt', 'r')
    f_out = open('output.txt', 'w')
    num_inp = int(f.readline())
    for i in xrange(num_inp):
        row1 = int(f.readline())
        cards_arr1 = []
        for j in xrange(4):
            row = f.readline()
            row = map(lambda x: int(x), row.split())
            cards_arr1.append(row)
        row2 = int(f.readline())
        cards_arr2 = []
        for j in xrange(4):
            row = f.readline()
            row = map(lambda x: int(x), row.split())
            cards_arr2.append(row)
        result = calculate(cards_arr1, cards_arr2, row1, row2)
        f_out.write('Case #%d: %s\n' % (i + 1, result))
    f.close()
    f_out.close()
