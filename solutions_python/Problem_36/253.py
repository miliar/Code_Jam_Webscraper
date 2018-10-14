WLC = 'welcome to code jam'
AL = 'abcdefghijklmnopqrstuvwxyz'
LSTRIP = AL.replace(WLC[0], '')
RSTRIP = AL.replace(WLC[-1], '')
OTHERS = AL.translate(None, WLC)

def read_file(filename):
    f = open(filename)
    contents = f.read().splitlines()
    return contents

contents = read_file('C-small-attempt0.in')
N = int(contents.pop(0))

def count_in_substring(sub, pos=0):
    def get_next():
        index = 0
        i = sub.find(WLC[pos], index)
        while i != -1:
            yield i
            index = i + 1
            i = sub.find(WLC[pos], index)
    counter = 0
    if pos < len(WLC):
        i_s = list(get_next())
        if not i_s:
            return 0
        for i in i_s:
            counter += count_in_substring(sub[i:], pos + 1)
    else:
        return 1
    return counter

for i, para in enumerate(contents):
    stripped = para.lstrip(LSTRIP).rstrip(RSTRIP).translate(None, OTHERS)
    print 'Case #%s: %.4d' % (i + 1, count_in_substring(stripped) % 10000)
