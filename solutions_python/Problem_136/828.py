def get_content(path):
    return [line.strip() for line in open(path, 'rb')]

def calc(content):
    cases = content.pop(0)
    ret = []
    for case in xrange(int(cases)):
        ret.append('')
        farms = 0
        cookies = 2
        c, f, x = content.pop(0).split(' ')
        c, f, x = float(c), float(f), float(x)
        time = 0

        while True:
            if (x / cookies) > (x / (cookies + f) + c / cookies):
                time += c / cookies
                cookies += f
                farms += 1
            else:
                break
        time += x / cookies
        ret[case] = 'Case #{}: {:.7f}'.format(case + 1, time)
    return ret

if __name__ == '__main__':
    content = get_content(r'c:\gjam\2\B-large.in')
    ret = calc(content)
    with open(r'c:\gjam\2\out.txt', 'wb') as fwriter:
        for line in ret:
            fwriter.write(line)
            fwriter.write('\r\n')
