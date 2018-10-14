import re

def process_case() :
    P = int(raw_input())
    M = map(int, raw_input().split())
    assert len(M) == 2**P

    tickets = []

    for i in range(0, P) :
        arr = map(int, raw_input().split())
        step = 2**P // len(arr) 
        for i, v in enumerate(arr) :
            target = (i*step, (i+1)*step)
            tickets.append( (v, target) )

    M = [ P-i for i in M ]

    cost = 0
    while True :
        # print M
        # print tickets
        ok = True
        for i in range(0, len(M)) :
            if M[i] != 0 :
                ok = False
        if ok :
            break

        best_index = None
        best_fit = 0

    
        for index, t in enumerate(tickets) :
            fit = 0
            r = t[1]
            for i in range(r[0], r[1]) :
                if M[i] != 0 :
                    fit += 1
            # print fit, best_fit
            if fit > best_fit :
                best_fit = fit
                best_index = index

        r = tickets[best_index][1]
        for i in range(r[0], r[1]) :
            if M[i] > 0 :
                M[i] -= 1
        del tickets[best_index]
        cost += 1
    
    return "%s" % cost

if __name__ == "__main__" :
    case_num = int(raw_input())
    for i in range(case_num) :
        result = process_case()
        print "Case #%d: %s" % (i+1, result)
