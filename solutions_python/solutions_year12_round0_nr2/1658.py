
def  max_given_score_googlers(N,S,p,scores):

    result = 0
    
    for k in range(N):
##        print result
##        print S
        googlerscore = int(scores[k])
        meanscore = googlerscore / 3
        diff = googlerscore % 3

##        print googlerscore
##        print meanscore
##        print diff
##        print "---"

        if meanscore >= p:
            result += 1
            continue

        if diff >= 1:
            if meanscore+1 >= p:
                result += 1
                continue
            
            if diff == 2 and meanscore+2 >= p:
                if S>0:
                    result += 1
                    S -= 1
                    continue

        #case which there is no diff,
                #but the possibility of shifting two values
                #aiming to see if one of them achieves the goal
        if meanscore - 1 >= 0:
            if meanscore+1 >= p:
                if S>0:
                    result += 1
                    S -= 1
                    continue    


    return result


def test(filename):
    fin = open(filename, 'r')
    fout = open(filename[:len(filename)-3] + ".out", 'w')
    T = int(fin.readline())
    for k in range(T):
        line = fin.readline()
        inputs = line.split()
        N = int(inputs[0])
        S = int(inputs[1])
        p = int(inputs[2])
        scores = inputs[3:]

##        print N, S, p, scores
        
        result = max_given_score_googlers(N,S,p,scores)
        fout.write("Case #%d: %s \n" % (k+1,result))
        
    fin.close()
    fout.close()


#main
test('B-large.in')
        
