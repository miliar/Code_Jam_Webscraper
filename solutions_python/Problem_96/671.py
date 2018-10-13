
def UnsurpTriple(total):
    if total % 3 == 0:
        return (total/3, total/3, total/3)
    elif total % 3 == 1:
        return (total/3, total/3, total/3 + 1)
    else:
        return (total/3, total/3 + 1, total/3 + 1)

def SurpTriple(total):
    if total < 2 or total > 28:
        return None  # Avoiding inputs which cannot be surprising
    elif total % 3 == 0:
        return (total/3 - 1, total/3, total/3 + 1)
    elif total % 3 == 1:
        return (total/3 - 1, total/3 + 1, total/3 + 1)
    else:
        return (total/3, total/3, total/3 + 2)

def GoodMaxOptions(total, p):
    if max(UnsurpTriple(total)) >= p and max(SurpTriple(total)) >= p:
        return "BOTH_OK"
    elif max(UnsurpTriple(total)) >= p:
        return "UNSURP_OK"
    elif max(SurpTriple(total)) >= p:
        return "SURP_OK"
    else:
        return "NEITHER_OK"

outputlist = []

for i, testcase in enumerate(open('B-large.in', 'r').read().splitlines()[1:]):
    raw_numbers = map(int, testcase.split())
    N, S, p = raw_numbers[0], raw_numbers[1], raw_numbers[2]
    
    if p == 0:
        outputlist.append('Case #%i: %i' % (i+1, N))
        continue
    elif p == 1:
        count_one_pluses = sum(1 for i in raw_numbers[3:] if i != 0)
        outputlist.append('Case #%i: %i' % (i+1, count_one_pluses))
        continue
    
    # Now p must be in [2,10]
    
    possible_goodmax = 0
    both_OK, neither_OK, surp_OK, unsurp_OK = 0, 0, 0, 0
    
    for total in raw_numbers[3:]:
        if total <= 1 or total >= 29: # <-- these require unsurprising scores,
            N -= 1                    # so we tabulate them immediately
            if total >= 29:
                possible_goodmax += 1
            #if total == 29 and p >= 9:
            #    possible_goodmax += 1
            #if total == 30 and p == 10:
            #    possible_goodmax += 1
        elif GoodMaxOptions(total, p) == "NEITHER_OK":
            neither_OK += 1
        elif GoodMaxOptions(total, p) == "BOTH_OK":
            both_OK += 1
        elif GoodMaxOptions(total, p) == "UNSURP_OK":
            unsurp_OK += 1
        else:
            surp_OK += 1
    assert both_OK + neither_OK + surp_OK + unsurp_OK == N
    
    if S <= surp_OK: # ...then assign all surprising scores to surp_OK totals
        possible_goodmax += (S + both_OK + unsurp_OK)
    elif S <= surp_OK + both_OK + neither_OK:
        possible_goodmax += (surp_OK + both_OK + unsurp_OK)
    else:
        extra = S - surp_OK - both_OK - neither_OK
        possible_goodmax += surp_OK + both_OK + (unsurp_OK - extra)
        #= surp_OK + both_OK + unsurp_OK - (S - surp_OK - both_OK - neither_OK)
        #= surp_OK + both_OK + unsurp_OK - (S + unsurp_OK - N)
        #= surp_OK + both_OK - S + N
    
    outputlist.append('Case #%i: %i' % (i+1, possible_goodmax))

outputfile = open('DancingWithTheGooglersOutput2.txt', 'w')

outputfile.write( '\n'.join(outputlist) )