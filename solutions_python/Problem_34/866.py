import sys
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def in_dict(str):
    for v in dict:
        if v.find(str) == 0:
            return True
    return False

def get_words(txt):
    out = ['']
    buff = ''
    conct = False
    L_cur = 1

    for v in txt:
        L_cur += 1
        if v == '(' and buff == '':
            conct = True

        elif v == ')':
            if buff != '':
                out = [itm + chr for chr in buff for itm in out if in_dict(itm + chr)]

            buff = ''
            conct = False

        elif conct == True:
            buff = buff + v

        elif v != '(' and v != ')':
            out = [ itm + v for itm in out if in_dict(itm + v)]

    return out

if len(sys.argv) == 3 :
    inp = file(sys.argv[1])
    ln1 = inp.readline().strip()

    if ln1:
        L, N , D = ln1.split()
        L = int(L)
        N = int(N)
        D = int(D)
    else:
        exit()

    lst = inp.read().splitlines()
    dict = lst[0:N]

    lst = lst[N:]
    lens = []
    outp = open(sys.argv[2], 'w+')
    intc = 1
    outp = open(sys.argv[2], 'w+')

    for v in lst:
        dt = []
        occs = 0
        print v

        occs = len(get_words(v))


        cstr = 'Case #' + str(intc) + ': ' + str(occs) + '\n'
        outp.write(cstr)
        print cstr
        intc += 1

    outp.close()
    inp.close()
