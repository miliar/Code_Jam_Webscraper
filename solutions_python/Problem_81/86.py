INPUT = {
    'raw_matches': ('string', 'array')
}

TEST = ('''\
2
3
.10
0.1
10.
4
.11.
0.00
01.1
.10.
''','''\
Case #1:
0.5
0.5
0.5
Case #2:
0.645833333333
0.368055555556
0.604166666667
0.395833333333
''')

SEPARATOR = '\n'

def memoized(fn):
    __mem = dict()
    def mem_fn(*args):
        v = None
        if (__mem.has_key(args)):
            v = __mem[args]
        else:
            v = fn(*args)
            __mem[args] = v
        return v
    return mem_fn

    
def fmt_output(data):
    return '\n'.join(map(str, data))

WIN = 1
LOSS = -1
NO_MATCH = 0

TRANSLATION = {
    '.': NO_MATCH,
    '1': WIN,
    '0': LOSS,
}
    
def translate(x):
    return TRANSLATION[x]
    
def main(raw_matches) :
    TOTAL = len(raw_matches)
    
    @memoized
    def match_result(me, opponent):
        return translate(raw_matches[me][opponent])
    
    @memoized
    def matches(me):
        return map(translate, raw_matches[me])
    
    @memoized
    def stats(me):
        wins = 0
        losses = 0
        
        for r in matches(me):
            if r == WIN:
                wins = wins + 1
            elif r == LOSS:
                losses = losses + 1
        return wins, losses, wins + losses
    
    @memoized
    def opponents(me):
        ops = []
        for them in xrange(TOTAL):
            if not match_result(me, them) == NO_MATCH:
                ops.append(them)
        return ops
    
    @memoized
    def WP(me):
        w, l, t = stats(me)
        return float(w) / t
            
    @memoized
    def OWP(me):
        owps = []
        thems = opponents(me)
        for them in thems:
            if them == me: continue
            
            w, l, t = stats(them)
            # determine WP for them
            if t == 0:
                owps.append(0.0)
            else:
                mr = match_result(them, me)
                if mr == WIN:
                    # they won a match against us, deduce this victory
                    owps.append(float(w-1) / (t-1))
                elif mr == LOSS:
                    # they lost that match to us
                    owps.append(float(w) / (t-1))
        return sum(owps) / float(len(thems))
    
    @memoized 
    def OOWP(me):
        thems = opponents(me)
        return sum(map(OWP, thems)) / float(len(thems))
        
    def RPI(me):
        return 0.25 * WP(me) + 0.50 * OWP(me) + 0.25 * OOWP(me)
    
    results = map(RPI, xrange(TOTAL))
    return fmt_output(results)
    

