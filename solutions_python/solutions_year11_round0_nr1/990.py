import sys

def findnextbutton(moves, c):
    for pair in moves:
        movec = pair[0]
        if movec == c:
            return pair[1]
    return None

def main(tests):
    results = []
    tests = tests.split('\n')
    tests = tests[1:]
    for test in tests:
        print test
    
    case = 0
    for test in tests:
        case = case + 1
        test = test.split(' ')
        nbut = test.pop(0) 
        moves = [(test[n],int(test[n+1])) for n in range(0,len(test)-1,2)]
        #print moves
        sec = 0
        opos = 1
        bpos = 1
        while True:
            
            omove = findnextbutton(moves, 'O')
            bmove = findnextbutton(moves, 'B')
            opushed = False
            
            if omove == None and bmove == None:
                break
            else:
                if omove == None:
                    pass
                elif omove > opos:
                    opos = opos + 1
                elif omove < opos:
                    opos = opos - 1
                elif omove == opos:
                    if ('O', omove) == moves[0]:
                        moves.pop(0)
                        opushed = True
                
                if bmove == None:
                    pass      
                elif bmove > bpos:
                    bpos = bpos + 1
                elif bmove < bpos:
                    bpos = bpos - 1
                elif bmove == bpos:
                    if ('B', bmove) == moves[0] and not opushed:
                        moves.pop(0)
                           
            sec = sec + 1
        
        results.append('Case #' + str(case) +': ' + str(sec) + '\n')
        
    return ''.join(results)

if __name__ == '__main__':
    inpath = sys.argv[1]
    fin = open(inpath, 'r')
    tests = fin.read()
    fin.close()
    results = main(tests)
    fout = open('outputfile.txt' ,'w')
    fout.write(results)
    fout.close()
        