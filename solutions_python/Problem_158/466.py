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


def getAValue(seg, ll, prev_char, start_pos, end_pos):
    pos = start_pos
    while pos <= end_pos:
        curr_char = seg[pos % ll]
        result_char = multipy(prev_char, curr_char)
        #print '            ( %s x %s ) => %s' % (prev_char, curr_char, result_char)
        prev_char = result_char
        pos += 1
    return result_char

def checkAValue(seg, ll, prev_char, start_pos, end_pos, target_char):
    return target_char == getAValue(seg, ll, prev_char, start_pos, end_pos)

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

def solveOne(data):
    ss = data.split()
    xx = int(ss[0])
    rr = int(ss[1])
    cc = int(ss[2])
    answer_un_winnable = None
    if len(ss) > 3:
        answer_un_winnable = ss[3] != 'GABRIEL'

    debug('input : %d-omino, %dx%d-grid' % (xx, rr, cc))

    un_winnable = False

    g_size = rr*cc

    if xx > rr and xx > cc:
        debug('If longer than the grid')
        un_winnable = True

    elif g_size % xx != 0:
        debug('# If left cell cannot even be filled (not divisible)')
        un_winnable = True

    elif xx >> g_size:
        debug('# If bigger')
        un_winnable = True

    elif g_size % xx != 0:
        debug('# If left cell cannot even be filled (not divisible)')
        un_winnable = True

    elif ( rr == 2 and xx >= 4 ) or ( cc == 2 and xx >= 4):
        debug('# Can cross a dead corner?')
        un_winnable = True

    for xrow in range(1,(xx+1)/2+1):
        xcol = xx-xrow+1
        if ( xrow > rr and xcol > rr) or ( xrow > cc and xcol > cc):
            debug('# If outer shape bigger than the grid')
            un_winnable = True

    if answer_un_winnable is not None:
        print "DEBUG: Correct? = ", answer_un_winnable == un_winnable

    if un_winnable:
        return 'RICHARD'
    else:
        return 'GABRIEL'

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
                ln = fp.readline().rstrip()
                answer = 'Case #%d: %s' % ((i+1), solveOne(ln))
                print answer
                fpw.write(answer + os.linesep)

