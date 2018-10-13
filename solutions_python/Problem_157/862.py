import sys, math

stdin = sys.stdin.readlines()
cases = int(stdin.pop(0))
for case in xrange(cases):
    l, x = stdin.pop(0).split(' ')
    x = int(x)
    fullstring = list(stdin.pop(0).strip() * x)
    ijk = "i"
    case_res = ": NO"
    h = 0
    length = len(fullstring)
    neg = False
    while h < length-1:
        if not neg and fullstring[h] == ijk:
            if ijk == "i":
                ijk = "j"
            elif ijk == "j":
                ijk = "k"
            elif ijk == "k":
                ijk = "1"
        else:
            if fullstring[h] == "i":
                if fullstring[h+1] == "i":
                    h += 1
                    neg = not neg
                elif fullstring[h+1] == "j":
                    fullstring[h+1] = "k"
                elif fullstring[h+1] == "k":
                    fullstring[h+1] = "j"
                    neg = not neg
            elif fullstring[h] == "j":
                if fullstring[h+1] == "i":
                    fullstring[h+1] = "k"
                    neg = not neg
                elif fullstring[h+1] == "j":
                    h += 1
                    neg = not neg
                elif fullstring[h+1] == "k":
                    fullstring[h+1] = "i"
            elif fullstring[h] == "k":
                if fullstring[h+1] == "i":
                    fullstring[h+1] = "j"
                elif fullstring[h+1] == "j":
                    fullstring[h+1] = "i"
                    neg = not neg
                elif fullstring[h+1] == "k":
                    h += 1
                    neg = not neg
        h += 1
    if not neg and ((ijk == "1" and h == length) or (ijk == "k" and fullstring[h] == "k")):
        case_res = ": YES"
    print "Case #"+str(case+1)+case_res
