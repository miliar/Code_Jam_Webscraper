def get_content(path):
    return [line.strip() for line in open(path, 'rb')]

def calc(content):
    cases = content.pop(0)
    ret = []
    for case in xrange(int(cases)):
        ret.append('')
        first = int(content.pop(0)) - 1
        matrix = []
        for _ in range(4):
            raw_row = content.pop(0)
            row = raw_row.split(' ')
            matrix.append(row)

        selected_row = matrix[first] 

        second = int(content.pop(0)) - 1
        matrix = []
        for _ in range(4):
            raw_row = content.pop(0)
            row = raw_row.split(' ')
            matrix.append(row)
        selected_row_2 = matrix[second]

        found = False
        for num in selected_row:
            if num in selected_row_2:
                ret[case] = 'Case #{}: {}'.format(case + 1, num)
                if found:
                     ret[case] = 'Case #{}: Bad magician!'.format(case + 1)
                     break
                found = True
        if not found:
            ret[case] = 'Case #{}: Volunteer cheated!'.format(case + 1)
    return ret

if __name__ == '__main__':
    content = get_content(r'c:\gjam\1\A-small-attempt0.in')
    ret = calc(content)
    print ret
    with open(r'c:\gjam\1\out.txt', 'wb') as fwriter:
        for line in ret:
            fwriter.write(line)
            fwriter.write('\r\n')
