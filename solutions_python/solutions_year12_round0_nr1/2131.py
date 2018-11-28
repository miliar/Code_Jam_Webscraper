import string

income = open('A-small-attempt0.in','rU')
outcome = open('A-small-attempt0.out','w')

def translate(input_string):
    code = [x for x in 'ynficwlbkuomxsevzpdrjgthaq']
    plain = [x for x in string.ascii_lowercase]
    trans = dict(zip(code,plain))
    base = [x for x in input_string] # converts string into a list
    out = [] # empty dict for plaintext
    for i in base:
        if i in string.ascii_lowercase:
            out.append(trans[i])
        else:
            out.append(i)
    return ''.join(out)
            
    

lineState = 0 # check for first line
for line in income:
    if lineState == 0:
        lineState += 1
        continue # supposed to short-circuit to next loop
    outcome.write('Case #%d: %s' % (lineState,translate(line)))
    lineState += 1

income.close()
outcome.close()
