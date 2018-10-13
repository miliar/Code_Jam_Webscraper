
import sys





if __name__ == "__main__":
    lines = open(sys.argv[1]).readlines()
    
    for p in range(int(lines.pop(0))):
        rep1 = int(lines.pop(0))
        rows = []
        for i in range(4):
            rows.append([c for c in lines.pop(0).split()])
        myrow = rows[rep1-1]
        
        rep2 = int(lines.pop(0))
        rows = []
        for i in range(4):
            rows.append([c for c in lines.pop(0).split()])
            
        myrow2 = rows[rep2-1]
        
        myrow = set(myrow)
        myrow2 = set(myrow2)
        
        #print myrow, myrow2
        
        
        l = len(myrow & myrow2)
        if l == 0:
            answer = "Volunteer cheated!"
        elif l == 1:
            answer = list(myrow & myrow2)[0]
        else: 
            answer = "Bad magician!"
            
        print "Case #%i:"%(p+1), answer
            
        
        