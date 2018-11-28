#!/usr/bin/env python

def memoize(func):
    memos = dict()
    def memoized(*args):
        if args in memos:
            return memos[args]
        result = func(*args)
        memos[args] = result
        return result
    return memoized 
    
########################  Solve  ########################

def next_button(data, start, button):
    i = start
    while i < len(data):
        if(data[i][0] == button):
            return i
        i = i + 1
    return None

#@memoize        
def solve(data):
    result = 0
    bot_O = 0
    bot_B = 0
    pos_O = 1
    pos_B = 1
    prev = None
    
    for step in data:
        if step[0] == 'O':
            clock = abs(pos_O - step[1])
            if prev == 'B':
                clock = clock - bot_B
                if clock < 0:
                    clock = 0
                prev = 'O'
                bot_O = clock + 1
            else:
                bot_O = bot_O + clock + 1
                prev = 'O'
            pos_O = step[1]
            result = result + clock + 1
        else:
            clock = abs(pos_B - step[1])
            if prev == 'O':
                clock = clock - bot_O
                if clock < 0:
                    clock = 0
                prev = 'B'
                bot_B = clock + 1
            else:
                bot_B = bot_B + clock + 1
                prev = 'B'
            pos_B = step[1]
            result = result + clock + 1
#        print result, ' ', pos_O, ' ', pos_B, ' ', bot_O, ' ', bot_B, ' ', prev
#    print ''
    return result
    
########################  Template  ########################
def memoize(func):
    memos = dict()
    def memoized(*args):
        if args in memos:
            return memos[args]
        result = func(*args)
        memos[args] = result
        return result
    return memoize    

def problem(fin):
    result = fin.readline().strip('\n').split(' ')
    l = []
    for i in xrange(int(result[0])):
        l.append((result[i * 2 + 1], int(result[i * 2 + 2])))
    return l
       
if __name__ == '__main__':
    from sys import argv
    
    fin = open(argv[1])
    fout = open(argv[1].replace("in", "out"), "w")
        
    numLines = int(fin.readline())
    problem_list = [problem(fin) for i in range(numLines)]
    
    solution_list = map(solve, problem_list)

    for i, s in enumerate(solution_list):
        fout.write("Case #%s: %s\n" % (i + 1, s))
