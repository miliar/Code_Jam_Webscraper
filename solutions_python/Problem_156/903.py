def get_content(path):
    return [line.strip() for line in open(path, 'rb')]


def calc(content):
    cases = content.pop(0)
    ret = []
    for case in xrange(int(cases)):
        print 'Case #{}'.format(case + 1)
        ret.append('')

        content.pop(0)  # diners
        pancakes = [int(i) for i in content.pop(0).split()]
        minutes = 0
        times = [max(pancakes)]
        
        pancakes2 = pancakes[:]
        while max(pancakes2) > 3:
            max_table = max(pancakes2)
            pancakes2.remove(max_table)
            if max_table % 2 == 0:
                pancakes2.append(max_table/2)
                pancakes2.append(max_table/2)
            else:
               pancakes2.append(max_table/2 + 1)
               pancakes2.append(max_table/2)
            minutes += 1
            times.append(max(pancakes2) + minutes)
        
        minutes = 0
        while max(pancakes) > 3:
            max_table = max(pancakes)
            pancakes.remove(max_table)
            pancakes.append(max_table - 3)
            pancakes.append(3)
            minutes += 1
            times.append(max(pancakes) + minutes)
        
        ret[case] = 'Case #{}: {}'.format(case + 1, min(times))
    return ret


if __name__ == '__main__':
    content = get_content(r'B-small-attempt8.in')
    ret = calc(content)
    print ret
    with open(r'B-small-attempt8.out', 'wb') as fwriter:
        for line in ret:
            fwriter.write(line)
            fwriter.write('\r\n')

