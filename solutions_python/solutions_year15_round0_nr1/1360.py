def get_content(path):
    return [line.strip() for line in open(path, 'rb')]

def calc(content):
    cases = content.pop(0)
    ret = []
    for case in xrange(int(cases)):
        ret.append('')

        standing = 0
        required = 0
        _, shyness = content.pop(0).split()
        for shyness_lvl, ppl_in_shyness_lvl in enumerate(shyness):
            ppl_in_shyness_lvl_int = int(ppl_in_shyness_lvl)
            if ppl_in_shyness_lvl_int > 0:
                if standing >= shyness_lvl:
                    standing += ppl_in_shyness_lvl_int
                else:
                    required += shyness_lvl - standing
                    standing += ppl_in_shyness_lvl_int + (shyness_lvl - standing)
        
        ret[case] = 'Case #{}: {}'.format(case + 1, required)
    return ret

if __name__ == '__main__':
    content = get_content(r'A-large.in')
    ret = calc(content)
    print ret
    with open(r'A-large.out', 'wb') as fwriter:
        for line in ret:
            fwriter.write(line)
            fwriter.write('\r\n')

