'''
Created on Apr 11, 2015

@author: Pango
'''

from os.path import basename
import re
import os
import sys

sys.setrecursionlimit(100000)

DEBUGMODE = True

QUATERNION_MAP = {
    '1':{'1':'1', 'i':'i', 'j':'j', 'k':'k'},
    'i':{'1':'i', 'i':'-1', 'j':'k', 'k':'-j'},
    'j':{'1':'j', 'i':'-k', 'j':'-1', 'k':'i'},
    'k':{'1':'k', 'i':'j', 'j':'-i', 'k':'-1'}}

### Functions ###
def debug(text):
    global DEBUGMODE
    if DEBUGMODE:
        print 'DEBUG:', text

def multipy(a, b):
    minus = False
    if a.startswith('-'):
        minus = not minus
        a = a.replace('-', '')
    if b.startswith('-'):
        minus = not minus
        b = b.replace('-', '')
    global QUATERNION_MAP
    c = QUATERNION_MAP[a][b]
    if minus:
        if c.startswith('-'):
            c = c.replace('-', '')
            minus = not minus
            return c
        else:
            return '-' + c
    else:
        return c

def scanForward(seg, ll, prev_char, start_pos, end_pos, target_char):
    found_pos = -1

    pos = start_pos
    while pos <= end_pos:
        curr_char = seg[pos % ll]
        if prev_char is not None:
            result_char = multipy(prev_char, curr_char)
        else:
            result_char = curr_char
        if result_char == target_char:
            found_pos = pos
            break
        prev_char = result_char
        pos += 1
    return found_pos

def scanBackward(seg, ll, next_char, start_pos, end_pos, target_char):
    found_pos = -1

    pos = end_pos
    while pos >= start_pos:
        curr_char = seg[pos % ll]
        if next_char is not None:
            result_char = multipy(curr_char, next_char)
            #print '( %s x %s ) = %s' % (curr_char, next_char, result_char)
        else:
            result_char = curr_char
        if result_char == target_char:
            found_pos = pos
            break
        next_char = result_char
        pos -= 1
    return found_pos

def checkAValue(seg, ll, prev_char, start_pos, end_pos, target_char):
    pos = start_pos
    while pos <= end_pos:
        curr_char = seg[pos % ll]
        result_char = multipy(prev_char, curr_char)
        #print '            ( %s x %s ) => %s' % (prev_char, curr_char, result_char)
        prev_char = result_char
        pos += 1
    return result_char == target_char

def goGetJ(seg, ll, pos_head, pos_tail):
    if pos_head > pos_tail:
        return False

    while not checkAValue(seg, ll, 'i', pos_head, pos_tail, 'j'):
        #print '(%d, %d) != "j" : "%s...%s"' % (pos_head, pos_tail, seg[pos_head % ll], seg[pos_tail % ll])
        # adjust tail
        pos_tail_backup = pos_tail
        while pos_head <= pos_tail:
            pos = scanBackward(seg, ll, 'k', pos_head, pos_tail, 'k')
            #debug( 'BACK(%d, %d)' % (pos_head, pos_tail) )
            if pos != -1:
                pos_tail = pos-1
                #print '(%d, %d) ?=? "j" : "%s...%s"' % (pos_head, pos_tail, seg[pos_head % ll], seg[pos_tail % ll])
                if checkAValue(seg, ll, 'i', pos_head, pos_tail, 'j'):
                    return True
            else:
                break # Break if not k at the last
        pos_tail = pos_tail_backup # Restore this

        # adjust head and loop again
        pos = scanForward(seg, ll, 'i', pos_head, pos_tail, 'i')
        if pos != -1:
            pos_head = pos+1
        else:
            return False # False if not found
        if pos_head > pos_tail:
            return False

    return True

def solveOne(data1, data2):
    ss = data1.split()
    ll = int(ss[0])
    xx = int(ss[1])
    seg = data2
    debug('input : %s x %d' % (seg, xx))

    if ll*xx < 3:
        return 'NO'

    found = False
    pos_head = 0
    pos_tail = ll*xx-1

    #if not checkAValue(seg, ll, seg[0], pos_head+1, pos_tail, '-1'): # Because ijk => -1
    #    return 'NO'

    # find the first 'i'
    pos = scanForward(seg, ll, None, pos_head, pos_tail, 'i')
    if pos != -1:
        pos_head = pos+1

        # find the last 'k'
        pos = scanBackward(seg, ll, None, pos_head, pos_tail, 'k')
        if pos != -1:
            pos_tail = pos-1

            # now adjust from med
            #found = goGetJ(seg, ll, pos_head, pos_tail)
            #print "        XXX", pos_head, pos_tail
            found = checkAValue(seg, ll, 'i', pos_head, pos_tail, 'k') # ij => k
    if found:
        return 'YES'
    else:
        return 'NO'

### Main ###
if __name__ == '__main__':
    filename = re.sub('\.py$', '', basename(__file__))

    input_filepath = './input/large/' + filename + '.dat'
    if not os.path.exists(input_filepath):
        input_filepath = input_filepath.replace('/large/', '/small/')
    if not os.path.exists(input_filepath):
        input_filepath = input_filepath.replace('/small/', '/sample/')
    output_filepath = input_filepath.replace('/input/', '/output/')

    with open(input_filepath) as fp:
        with open(output_filepath, 'w') as fpw:
            ln = fp.readline().rstrip()
            caseNumber = int(ln)
            for i in range(caseNumber):
                ln1 = fp.readline().rstrip()
                ln2 = fp.readline().rstrip()
                answer = 'Case #%d: %s' % ((i+1), solveOne(ln1, ln2))
                print answer
                fpw.write(answer + os.linesep)

