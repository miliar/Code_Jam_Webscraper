import sys

first = True
r = 1
for line in sys.stdin:
    line = line.strip()
    if first:
        n_cases =  int(line)
        first = False
        continue
    n_types, shy = line.split(" ")
    n_types = int(n_types)
    dict_shy = {ix: int(shy[ix]) for ix in range(len(shy))}
    aud = 0
    total = 0
    for s, count in dict_shy.iteritems():
        if count == 0:
            continue
        else:
            if total >= s:
                total += count
                continue
            elif total < s:
                aud += s - total
                #print "Add " + str(aud) + "At " + str(s)
                total = s + count

    print "Case #" + str(r)+": " + str(aud)
    r = r+ 1

