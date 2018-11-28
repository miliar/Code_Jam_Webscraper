from itertools import groupby

def sub_unit(digits):
    if digits[0] > 1:
        return "%s%s" % (digits[0]-1, "".join("9" for x in range(len(digits)-1)))
    else:
        return "".join("9" for x in range(len(digits)-1))

T = int(raw_input())

for case in range(T):
    N = raw_input()

    digits = [int(i) for i in N]

    if sorted(digits) == digits:
        answer = "".join(str(x) for x in digits)
    else:
        subset_asc = any([digits[x] < digits[x+1] for x in range(len(digits)-1)])
        
        if not subset_asc:
            answer = sub_unit(digits)
        else:
            answer = ""
            for x in range(len(digits)-1):
                if digits[x] < digits[x+1]:
                    answer = "%s%s" % (answer, str(digits[x:x+1][0]))
                else:
                    answer = "%s%s" % (answer, sub_unit(digits[x:len(digits)]))
                    break

    print "Case #%d: %s" % (case+1, answer)