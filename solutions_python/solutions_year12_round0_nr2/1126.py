import sys

def main(raw_data):
    data = []
    for line in raw_data:
        data.append(line.strip())
        
    T = data.pop(0)
    for i, line in enumerate(data):
        info = line.split(' ')
        n = info.pop(0)
        number_of_surprises = int(info.pop(0))
        min_score = int(info.pop(0))
        totals = info
        #print number_of_surprises
        #print min_score
        #print totals
        count = 0
        for t in totals:
            total = int(t)
            
            #could it be reached normally?
            if total >= (min_score*3)-2:
                count +=1
            #could it be reached by surprise?
            elif total >= 2 and total >= (min_score*3)-4 and number_of_surprises > 0:
                count +=1
                number_of_surprises -= 1
                    
        
        print "Case #%s: %s" % (i+1, count)
                
if __name__ == "__main__":
    main(sys.stdin)
