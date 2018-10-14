def get_content(path):
    return [line.strip() for line in open(path, 'rb')]

def calc(content):
    cases = content.pop(0)
    ret = []
    for case in xrange(int(cases)):
        ret.append('')
        blocks = int(content.pop(0))
        naomi = [float(i) for i in content.pop(0).split(' ')]
        ken = [float(i) for i in content.pop(0).split(' ')]

        naomi2 = naomi[:]
        ken2 = ken[:]
    
        naomi_score_war = 0
        naomi_score_dwar = 0

        while ken and naomi:
            naomi_block = naomi.pop()
            bigger = [a for a in ken if a > naomi_block]
            if bigger:
                ken_choose = min(bigger)
            else:
                ken_choose = min(ken)
            ken.remove(ken_choose)
            if naomi_block > ken_choose:
                naomi_score_war += 1

        while ken2 and naomi2:
            ken_max = max(ken2)
            ken_min = min(ken2)
            naomi_max = max(naomi2)
            naomi_min = min(naomi2)

            if (naomi_min > ken_min and naomi_max > ken_max):
                naomi_choose = naomi_min
                ken_choose = ken_min
            elif (naomi_max > ken_max):
                naomi_opts = [i for i in naomi2 if i > ken_min]
                naomi_choose = min(naomi_opts)
                ken_choose = ken_min
            else:
                naomi_choose = naomi_min
                ken_choose = ken_max
    
            if naomi_choose > ken_choose:
                naomi_score_dwar += 1

            ken2.remove(ken_choose)
            naomi2.remove(naomi_choose)
            

        ret[case] = 'Case #{}: {} {}'.format(case + 1, naomi_score_dwar, naomi_score_war)
    return ret

if __name__ == '__main__':
    content = get_content(r'c:\gjam\4\D-large.in')
    ret = calc(content)
    with open(r'c:\gjam\4\out.txt', 'wb') as fwriter:
        for line in ret:
            fwriter.write(line)
            fwriter.write('\r\n')
