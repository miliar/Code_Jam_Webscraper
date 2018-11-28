import sys
import re
import itertools

# make combos use sets

def get_final_sequence():

    cur_seq = ''
    for i, el in enumerate(seq):

        # Only check for combos if there are combos and we already have
        # something in our sequence
        if combos and (len(cur_seq) > 0):
            result = check_combo(cur_seq[-1], el)
            if result:
                cur_seq = cur_seq[:-1]
                cur_seq += result
            else:
                cur_seq += el
        # Otherwise just add the element to our sequence
        else:
            cur_seq += el

        
        # Now check if there are any opposers
        if opposers:
            for c in itertools.combinations(cur_seq, 2):
                c = sorted(list(c))
                if c in opposers:
                    cur_seq = ''
    
    return cur_seq

def check_combo(a, b):
    for combo in combos:
        if combo.startswith((a+b, b+a)):
            return combo[2]

    # If none of the combos matched
    return False

def process_line(raw_line):
    raw_data = line.split()
    # line = line.rstrip('\n')
    # sep = re.compile('\d+')
    # data = sep.split(line)[1:]
    data = []
    for i, el in enumerate(raw_data):
        if el.isdigit():
            num = int(el)
            if num == 0:
                data.append(None)
            else:
                data.append([chunk for chunk in raw_data[i+1:i+1+num]])
    
    combos, opposers, seq = data
    if opposers:
        opposers = [sorted((a, b)) for a, b in opposers]

    return combos, opposers, seq[0]

if __name__ == '__main__':
    in_path = sys.argv[1]
    with open(in_path, 'r') as in_file:
        in_file.next()
        case = 1
        for line in in_file:
            combos, opposers, seq = process_line(line)

            solution = '['+', '.join(get_final_sequence())+']'
            print "Case #%s: %s" % (case, solution)
            case += 1