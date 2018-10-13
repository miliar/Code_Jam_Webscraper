'''
Created on 2012-4-11

@author: nvince
'''

def main( filename ):
    
    my_built = []
    for score in xrange(0, 31):
        avg = int(score/3)
        normal_max = avg
        suprise_max = -1
        
        if score % 3==0:
            normal_max = avg
            if avg-1>=0 and avg+1<=10:
                suprise_max = avg + 1
        elif score % 3 ==1:
            normal_max = avg + 1
            if avg-1>=0 and avg+1<=10:
                suprise_max = avg + 1
        else:
            normal_max = avg + 1
            if avg+2<=10:
                suprise_max = avg + 2
        print score, suprise_max
        my_built.append( (normal_max, suprise_max) )
            
    fin = open(filename)
    fout = open( filename.replace(".in", ".out"), "w")
    totalCase = int(fin.readline())
    for caseNum in xrange(1, totalCase+1):
        items = map(lambda s: int(s), fin.readline().strip().split(" "))
        dancers_count = items[0]
        suprises_total_count = items[1]
        p = items[2]
        
        scores = []
        for i in xrange(3, dancers_count+3):
            scores.append(items[i])
        
        result = 0
        suprises_count = 0
        for i in xrange(len(scores)):
            score = scores[i]
            normal_max = my_built[score][0]
            suprise_max = my_built[score][1]
            if normal_max>=p:
                result += 1
            else:
                if suprise_max!=-1 and suprise_max>=p and suprises_count<suprises_total_count:
                    result += 1
                    suprises_count+=1
        print result
        fout.write("Case #%i: %i\n" % (caseNum, result))
        
    fin.close()
    fout.close()
    print "%s finished." % (fout.name,)

if __name__ == '__main__':
    main("input.in")