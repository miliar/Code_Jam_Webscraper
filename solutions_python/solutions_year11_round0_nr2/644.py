from tools import *
import sys

lines = read_file(sys.argv[1])
del lines[0]

swap_list = []

def to_char_list(lst):
    ret = "["
    try:
        ret += lst[0]
    except:
        pass
    for ch in lst[1:]:
        ret += ", " + ch
    ret += "]"

    return ret

def process_swap(swap):
    return ((swap[0], swap[1]), swap[2])

def process_opposed(opp):
    return (opp[0], opp[1])

result = []

for i in xrange(0, len(lines)):
    swap_list = []
    opposed_list = []
    invoke_list = []

    lines[i] = lines[i].split(" ")

    lines[i][0] = int(lines[i][0])
    if lines[i][0] != 0:
        for j in xrange(1, lines[i][0] + 1):
            swap_list.append(process_swap(lines[i][j]))

    tmp = 1 + lines[i][0]
    lines[i][tmp] = int(lines[i][tmp])

    if lines[i][tmp] != 0:
        for j in xrange(tmp + 1, lines[i][tmp] + tmp + 1):
            opposed_list.append(process_opposed(lines[i][j]))

    elems = lines[i][-1]

    for elem in elems:
        invoke_list.append(elem)

        if len(invoke_list) >= 2:

            for (couple, to) in swap_list:

                if ( elem, invoke_list[-2] ) == couple \
                        or ( invoke_list[-2], elem ) == couple:
                    del invoke_list[-1]
                    invoke_list[-1] = to

            el = invoke_list[-1]
            for couple in opposed_list:
                if el in couple:
                    for e in invoke_list[:-1]:
                        if (e, el)  == couple or (el, e) == couple:
                            invoke_list = []
                            break


    print "ELEMS: %s" % elems
    print "SWAP: %s" % swap_list
    print "OPP: %s" % opposed_list
    print "INVOKE: %s" % invoke_list
    print ""
    result.append(to_char_list(invoke_list))

write_file(insert_case(result), "out")
