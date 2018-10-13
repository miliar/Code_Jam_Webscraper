import re, sys



def compute_switches(case, engines, queries):
    def wipe_hash(h):
        for e in engines:
            h[e] = False
    
    engine_hash = {}
    wipe_hash(engine_hash)
    total_engines = len(engines)
    seen = 0
    switches = 0
    for q in queries:
        if not engine_hash[q]:
            seen +=1
            if seen == total_engines:
                switches += 1
                wipe_hash(engine_hash)
                seen = 1
            engine_hash[q] = True
    print "Case #"+str(case)+":",switches


def parse_input():
    if len (sys.argv) < 2:
        print "Enter an input filename please"
        return
    inp = open (sys.argv[1])

    lines = [re.sub(r'[\n\r]','',l) for l in inp.readlines()]
    num_cases = int(lines[0])
    line_num = 1
    for case in xrange(num_cases):
        S = int(lines[line_num])
        line_num += 1
        engines = lines[line_num:line_num+S]
        line_num += S
        Q = int(lines[line_num])
        line_num += 1
        queries = lines[line_num:line_num+Q]
        line_num += Q
        compute_switches(case+1, engines, queries)

parse_input()