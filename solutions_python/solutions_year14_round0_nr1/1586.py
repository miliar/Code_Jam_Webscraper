'''
Created on 12 apr 2014

@author: algestam
'''

def get_answer_row():
    rownum = int(raw_input())
    row = set()
    for l in xrange(1,5):
        line = raw_input()
        if l == rownum:
            row = set(line.split())
            #print row
    return row
            
for case in xrange(input()):
    a1_set = get_answer_row()
    a2_set = get_answer_row()
    
    intersection = a1_set.intersection(a2_set)
    
    if len(intersection) == 1:
        res = intersection.pop()
    elif len(intersection) > 1:
        res = 'Bad magician!'
    else:
        res = 'Volunteer cheated!'

    print "Case #%i: %s" % (case+1, res)