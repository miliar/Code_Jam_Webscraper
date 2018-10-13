from itertools import zip_longest

def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def do_case(number, line):
    tokens = line.split()
    n = tokens[0]
    terms = [(i, int(j)) for (i, j) in grouper(2, tokens[1:])]
    opos = 1
    bpos = 1
    otarget = 1
    btarget = 1
    second_count = 0
    while terms:
        # print(terms)
        message = []
        otargetacq = False
        btargetacq = False
        buttonhit = False
        nextbot = terms[0][0]
        for term in terms:
            if term[0] == 'O':
                if otargetacq:
                    continue
                otarget = term[1]
                otargetacq = True
            elif term[0] == 'B':
                if btargetacq:
                    continue
                btarget = term[1]
                btargetacq = True
            if otargetacq and btargetacq:
                break
        otargetacq = True
        btargetacq = True
        if otarget > opos:
            message.append("Orange from {} to {}".format(opos, opos + 1))
            opos += 1
        elif otarget < opos:
            message.append("Orange from {} to {}".format(opos, opos - 1))
            opos -= 1
        elif nextbot == 'O':
            message.append("Orange hit button {}".format(opos))
            buttonhit = True
        else:
            message.append("Orange waiting at {}".format(opos))
        if btarget > bpos:
            message.append("Blue from {} to {}".format(bpos, bpos + 1))
            bpos += 1
        elif btarget < bpos:
            message.append("Blue from {} to {}".format(bpos, bpos - 1))
            bpos -= 1
        elif nextbot == 'B':
            message.append("Blue hit button {}".format(bpos))
            buttonhit = True
        else:
            message.append("Blue waiting at {}".format(bpos))
            # print('; '.join(message))
        if buttonhit:
            del terms[0]
        second_count += 1
    print("Case #{}: {}".format(number + 1, second_count))

with open('input.txt') as inputfile:
    lines = iter(inputfile)
    t = lines.__next__()
    for line in enumerate(lines):
        do_case(*line)
