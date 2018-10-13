


        
def option_1(total, typed, prob):
    
    aye = 1
    for p in prob:
        aye *= p
    rem = 1 - aye
    suc = aye * (total - typed + 1)
    nosuc = rem * (total - typed + total + 2)
    return (suc + nosuc)

def option_2(total, typed, back, prob):
    
    
    aye = 1
    for i in xrange(typed-back):
        aye *= prob[i]
    
    rem = 1-aye
    
    going_to = (total-typed+2*back + 1)
    suc = aye * going_to
    nosuc = rem * (going_to + total + 1)
        
    return (suc + nosuc)

def option_3(total):
    return float( 2 + total)

def find_all(total, typed, prob):
    
    final = []
    final.append(option_3(total))
    final.append(option_1(total, typed, prob))
    
    for back in xrange(1, typed+1):
        final.append(option_2(total,typed, back, prob))
    print final
    return min(final)
            



def clean(det, prob):
    det = det.split()
    prob = prob.split()
    for i in range(len(det)):
        det[i] = int(det[i])
    
    for i in xrange(len(prob)):
        prob[i] = float(prob[i])
    
    return (det[0],det[1], prob)




if __name__ == "__main__":        
    
    pagename = "A-small-attempt.in"
    page = open(pagename, "r")
    number_of_tests = int(page.readline().strip())
    answer_pagename = "password_answers.in"
    answer_page = open(answer_pagename, "w")
    for i in xrange(1, number_of_tests + 1):
        det = page.readline()
        prob = page.readline()
        typed, total, prob = clean(det, prob)
        answer_page.write("Case #%d: %f\n" % (i, find_all(total, typed, prob)))
    answer_page.close()

        