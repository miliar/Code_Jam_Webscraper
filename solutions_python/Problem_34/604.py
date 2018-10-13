import re

def pattern_matches_kw(pattern,kw):
    match = True
    
    for c_index in range(l):
        current_pattern = pattern[c_index]
        if len(current_pattern) == 1 and current_pattern != kw[c_index]:
            match = False
            break
        elif len(current_pattern) > 1 and kw[c_index] not in list(current_pattern):
            match = False
            break

    return match

l,d,n = map(int, raw_input().split())

known_words = []

for k in xrange(d):
    known_words.append(raw_input().strip())

#reading each pattern line
for case in xrange(n):
    matches = 0
    pattern =  re.findall(r'(\([a-z]+\)|[a-z])', raw_input())
    for p in range(len(pattern)):
        if len(pattern[p])>1:
            pattern[p] = pattern[p][1:-1]

    #trying all known words on pattern
    for kw in known_words:
        if pattern_matches_kw(pattern, kw):
            matches += 1

    print "Case #%i: %i" % (case+1, matches)
