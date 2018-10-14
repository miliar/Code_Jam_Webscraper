def get_sets():
    sets = []
    
    for i in xrange(4):
        sets.append(set(map(int,raw_input().strip().split())))

    return sets

if __name__ == "__main__":
    cases = int(raw_input())
    
    for case_no in xrange(cases):
        chosen1 = int(raw_input())
        sets1 = get_sets()
    

        chosen2 = int(raw_input())
        sets2 = get_sets()

        result = sets1[chosen1-1].intersection(sets2[chosen2-1])
        
        if(len(result) == 0):
            print "Case #" + str(case_no+1) + ": Volunteer cheated!"
        elif(len(result) > 1):
            print "Case #" + str(case_no+1) + ": Bad magician!"
        else:
            print "Case #" + str(case_no+1) + ": " + str(result.pop())
