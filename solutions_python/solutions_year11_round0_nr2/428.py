import sys

def match_opposites(result, c, c_opposites):
    for b in result:
        if b in c_opposites: return True

def do_magicka(s, reactions, opposites):
    result = []
    for c in s:
        if not result:
            result.append(c)
            continue
        
        react = result[-1] + c
        if react in reactions:
            result[-1] = reactions[react]
        elif match_opposites(result, c, opposites.get(c, {})):
            result = []
        else:
            result.append(c)
        
    return result

def main(input, output):
    cases_count = int(input.readline())
    for i in xrange(cases_count):
        case_id = i+1
        
        case = input.readline()
        case = iter(case.split())
        
        reactions = {}
        for j in xrange(int(case.next())):
            reaction = case.next()
            if len(reaction) != 3: raise ValueError()
            reactions[reaction[:2]] = reaction[2]
            reactions[reaction[:2][::-1]] = reaction[2]
            
        opposites = {}
        for j in xrange(int(case.next())):
            opps = case.next()
            if len(opps) != 2: raise ValueError()
            a, b = opps
            opposites.setdefault(a, {})[b] = True
            opposites.setdefault(b, {})[a] = True
        
        str_len = int(case.next())
        s = case.next()
        assert len(s) == str_len
        
        result = do_magicka(s, reactions, opposites)
        result = '[%s]' % ', '.join(result) 
        
        print >> output, 'Case #%s: %s' % (case_id, result)

if __name__ == '__main__':
    if '-q' in sys.argv:
        log = lambda msg: None
        sys.argv.remove('-q')
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
    else:
        input_path = 'example.txt'
    with file(input_path) as input:
        main(input, sys.stdout)
        