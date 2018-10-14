#
import math

sample = '''5
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21
1 0 9 23
2 2 0 17 6
3 1 6 30 14 14'''

def Translate(line, counter):
    output = 'Case #' + str(counter) + ': '

    data = line.split(' ')
    numg = int(data.pop(0))
    nums = int(data.pop(0))
    p = int(data.pop(0))
    
    surprising = nums

    print '-------------'
    print numg, nums, p, data
    print '--------'

    toggle = True # round up first

    solved_results = []

    for test in data:
        score = int(test)
        numg_ = 3
        results = []
        #for i in range(0, numg):
        for i in range(0, numg_):
            av = score / float(numg_)
            
            if toggle:
                av = math.ceil(av)
            else:
                av = math.floor(av)

            #print int(av)
            results.append(int(av))
            
            assert(int(av) <= 10 and int(av) >= 0)

            score -= av
            numg_ -= 1
    
        total = 0
        for r in results:
            total += r

        #print type(total), type(test)
        assert(total == int(test))
        #print results 
        #break
        

    ### !!!!!  do the 'surprising' step as a post solve....!!

        #  

        candidate = False
        rmax = max(results)
        rmin = min(results)
        

        for i in range(0, len(results)):
            if surprising == 0:
                break;

            s = results[i]
            
            if s >= p or p - rmin > 2 or rmax == 0:
                # no possible way?
                break
            
            print ' -------  possible candidate' + ' p = ' + str(p) + ' with ' + str(results)

            done = False
            for j in range(i + 1, len(results)):
                n = results[j]

                # the free case
#                if s < p and s - n < 1:
#                    print 'free candidate!  ' + str(i) + ' ' + str(j) + ' ' + str(surprising) 
#                    results[i] = results[i] + 1
#                    results[j] = results[j] - 1
#                    done = True
#                    break
#
                if s < p and s - n < 2 and surprising > 0:
                    print 'candidate!  ' + str(i) + ' ' + str(j) + ' ' + str(surprising) 
                    results[i] = results[i] + 1
                    results[j] = results[j] - 1
                    done = True
                    surprising -= 1
                    break

            if done:
                #print 'BREAK' 
                break

           # if cur - next < 2  
               # add one to curr, dec next and dec 'nums'

        print results
        total = 0
        for r in results:
            total += r

        #print type(total), type(test)
        assert(total == int(test))
        #print results 

        solved_results.append(results)
        

 #   print '------------solving-----------' 

    # FINAL
    resultnum = 0
    for solved in solved_results:
        max_ = max(solved)
#        print solved, ' p = ' + str(p) + ' ' + str(max_)
        if max_ >= p:
            resultnum += 1
#            print '++++'

    print '         - ' + str(resultnum)

    assert(resultnum <= numg)

    output += str(resultnum)
    output += '\n'
    return output 
    

if __name__ == "__main__":
 
    inputdata = None
    
    file_ = 'B-small-attempt3.in'
    with open(file_) as f:
        inputdata = f.read().split('\n')

    if None == inputdata:
        inputdata = sample.split('\n')

    #print inputdata
    #print type(inputdata)

    count = int(inputdata.pop(0))

    output = open(file_ + '.out', 'w')

    counter = 1
    for line in inputdata:
        #print line, len(line)
        if(len(line)):

            print '_______________________________________________________________________' 
            trans = Translate(line, counter)
            counter += 1
            output.write(trans)


        #break

    #for test in inputs:
    #    Translate(test, counter)
    #    counter += 1

    #if len(sys.argv) < 2:
    #    sys.exit('Need command line arguments!')
