def good_read(f):
    return f.readline().replace("\n","")

def read_line_and_split(f):
    return good_read(f).split(" ")

def read_int_line(f):
    return int(good_read(f))

def read_int_arr(f):
    return map(int, read_line_and_split(f))

#==========================

def read_int_and_array(elems):
    N = int(elems.pop(0))
    arr = []
    for k in range(N):
        arr.append(elems.pop(0))
    return arr

def read_configuration(fr):
    elems = read_line_and_split(fr)
    combines = read_int_and_array(elems)
    opposed = read_int_and_array(elems)
    series = elems[-1]
    return combines, opposed, series

def main(inf, outf):
    fr = open(inf)
    fw = open(outf, 'w')
    T = read_int_line(fr)
    for i in range(T):
        res = "Case #%d: [%s]\n" % (i+1, ", ".join(result(*read_configuration(fr))))
        fw.write(res)
    fw.close()
    fr.close()

def result(combines, opposed, series):
#    print combines, opposed, series
    elem_list = ""
    for e in series:
        cleared = False
        if elem_list:
            for comb in combines:
                cond1 = elem_list[-1] + e
                cond2 = e + elem_list[-1]
                if comb[:2] in (cond1, cond2):
                    elem_list = elem_list[:-1]
                    e = comb[2]
                    break

            for op in opposed:
                if (op[0] in elem_list and op[1] == e) or (op[1] in elem_list and op[0] == e):
                    elem_list = ""
                    cleared = True
                    break
        if not cleared:
            elem_list += e
    return [e for e in elem_list]


if __name__ == "__main__":
    main("B-large.in","but_result.txt")
  