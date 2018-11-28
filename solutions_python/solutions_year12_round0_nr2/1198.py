#!/usr/bin/env python

scores = [ 8, 0 ]
surprises = 1
ref_score = 1

def is_cool_without_surprise(s, ref_score):
    if s == 2:
        hscore = 1
    elif s == 1:
        hscore = 1
    elif s == 0:
        hscore = 0
    else:
        mod = s % 3

        if mod > 2:
            print "Esto no me lo habia esperado"
            return False

        elif mod == 2 or mod == 1:
            hscore = (s / 3) + 1
            
        else:
            hscore = (s / 3)

            #    print "Test: " + str(s) + ", " + str(ref_score)
            #    print "HScore: " + str(hscore)
    
    if hscore >= ref_score:
        return True
    else:
        return False


def is_cool_with_surprise(s, ref_score):
    if s == 2:
        hscore = 2
    elif s == 1:
        hscore = 1
    elif s == 0:
        hscore = 0
    else:
        mod = s % 3

        if mod > 2:
            print "Esto no me lo habia esperado"
            return False

        elif mod == 2:
            hscore = (s - ((s / 3) * 2))
        else:
            hscore = (s / 3) + 1

            #    print "Test Surprise: " + str(s) + ", " + str(ref_score)
            #    print "HScore: " + str(hscore)

    if hscore >= ref_score:
        return True
    else:
        return False


def calculate_googlers(score, surprises, ref_score):
    cool_googlers = 0
    
    for s in scores:
        if is_cool_without_surprise(s, ref_score):
            cool_googlers += 1
        elif surprises and is_cool_with_surprise(s, ref_score):
            surprises -= 1
            cool_googlers += 1

    return cool_googlers



numtests = None
numcase = 0

f = open('input.txt')
lines = f.readlines()
f.close()

for l in lines:
    if numtests == None:
        numtests = int(l)
    else:
        args = l.split()
        surprises = int(args[1])
        ref_score = int(args[2])

        scores = [ ]
        tmp = args[3:]
        for t in tmp:
            scores.append(int(t))

        numcase += 1
        print "Case #%d: %d" % (numcase, calculate_googlers(scores, surprises, ref_score))
        
