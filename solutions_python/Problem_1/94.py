import sys

def read_test_case(lines):
    se_c = int(lines[0])
    se = [l.strip() for l in lines[1:se_c+1]]
    qu_c = int(lines[se_c+1])
    qu = [l.strip() for l in lines[se_c+2:se_c+2+qu_c]]
    return se,qu,lines[se_c+2+qu_c:]

def index_in_list(l, x):
    'Finds the element x in the list l, returns a large number (the length of the list) if it does not'
    try:
        return l.index(x)
    except ValueError:
        return len(l) + 1

def without(l, m):
    'Eliminates the first ocurrence of m in l'
    if l == [] : return []
    if l[0] == m : return l[1:]
    else: return [l[0]] + without(l[1:], m)

def count_switches(s_en, que):
    """Counts how many times do you need to switch engines. 
    It considers the engine that occurs latest on the list to be the best choice"""
    index,choice = max(zip([index_in_list(que, s) for s in s_en], xrange(len(s_en))))
    sws = 0
    choices = [s_en[choice]]
    while index < len(que) :
        que = que[index:]
        index, choice = max(zip([index_in_list(que, s) for s in s_en], xrange(len(s_en))))
        choices.append(s_en[choice])
        sws += 1
    return sws

if __name__ == '__main__':
    lines = [line for line in open(sys.argv[1])]
    t_c = int(lines[0])
    lines = lines[1:]
    test_cases = []
    for i in xrange(t_c):
        se,qu,lines = read_test_case(lines)
        print 'Case #'+str(i+1)+':', count_switches(se, qu)
