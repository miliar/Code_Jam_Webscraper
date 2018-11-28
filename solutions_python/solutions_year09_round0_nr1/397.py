#!/usr/bin/python2.5

def match_pattern(word, pattern):
    in_choice = False
    pos = 0
    partial_match = False
    for c in pattern:
        if (c == '('):
            in_choice = True
        elif (c == ')'):
            in_choice = False
            if (not partial_match): return False
        else:
            if (c == word[pos]):
                partial_match = True
        if (not in_choice): 
            pos += 1
            if (not partial_match): return False
            if (pos==L+1): return False
            partial_match = False
    return (pos == L)

(L, D, N) = map(int, raw_input().split())
legal_words = {}
for i in range(D):
    legal_words[raw_input()] = 1

for case in range(N):
    pattern = raw_input()
    nmatches = 0
    for word in legal_words.keys():
        if (match_pattern(word, pattern)):
            nmatches += 1
    print 'Case #%s: %d' % (case+1, nmatches)
