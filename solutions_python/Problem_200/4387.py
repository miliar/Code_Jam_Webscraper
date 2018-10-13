def compare(ins):
    for v in ins[2:]:
        if ins[1] > v:
            return False
    return True


def sort_digits(str_ins):
    if int(str_ins) <= 9:
        return str_ins
    # while 1:
    #     ins = str(ins)
    #     if int(str_ins) <= 9:
    #         return str(int(''.join(map(str, ins))))
    ins = map(int, str_ins)
    for index, num in enumerate(reversed(ins)):
        ind = -(index+1)
        indp = -(index + 2)
        if index == len(ins) - 1:
            if ins[0] != 0 and ins[0] <= ins[1] and compare(ins):
                return str(int(''.join(map(str, ins))))
            elif ins[0] == 0:
                ins = list((len(ins)-1)*"9")
                return str(int(''.join(map(str, ins))))
            elif ins[0] > ins[1] or not compare(ins):
                for c in range(1, len(ins)):
                    ins[c] = 9
                return str(int(''.join(map(str, ins))))
            break
        elif num < ins[indp]:
            ins[ind] = 9
            ins[indp] = ins[indp] - 1



t = int(raw_input())
for i in range(1, t+1):
    in_s = raw_input()
    in_s = sort_digits(in_s)
    print "Case #{}: {}".format(i, in_s)
