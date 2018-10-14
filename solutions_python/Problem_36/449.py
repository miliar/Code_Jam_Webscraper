to_find = "welcome to code jam"

def counter(li, target):
    if not len(target):
        yield 1
    elif len(li):
        start = 0
        for i in range(li.count(target[0])):
            start = li.index(target[0], start) + 1
            for j in counter(li[start:], target[1:]):
                yield 1

bob = open("C-small-attempt0.in")
first = True
case_num = 0
for line in bob:
    if first:
        first = False
        continue
    res = 0
    for i in counter(line, to_find):
        res += 1
    case_num += 1
    print "Case #%i: %04i" % (case_num, res%1000)
