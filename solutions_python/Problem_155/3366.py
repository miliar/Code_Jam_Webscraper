def standing_ovation(shyness_arr):
    standing=0
    extra=0
    for needed, provided in enumerate(shyness_arr):
        #print needed,provided, standing,extra
        if needed>standing+extra:
            extra=needed-standing;
        standing+=provided
    return extra

def standing_ovation_string(shyness_str):
    return standing_ovation(map(lambda c: ord(c)-ord('0'),shyness_str))

def standing_ovation_line(line):
    return standing_ovation_string(line.strip().split(' ')[1])

import fileinput

for idx,line in enumerate(filter(lambda f: not fileinput.isfirstline(), fileinput.input() )):
    print 'Case #%d: %s'%(idx+1,standing_ovation_line(line))