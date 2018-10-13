class RopeInternet:
    
    @staticmethod
    def calculate(all):
        sum = 0
        
        
        for x in all:
            if x[0] - x[1] > 0 :
                for y in all:
                    if y[0] < x[0] and y[1] > x [1]:
                        if y[0] == y[1] :
                            sum+=1
                        else :
                            sum+=0.5
            if x[0] - x[1] == 0 :
                pass
            if x[0] - x[1] < 0 :
                for y in all:
                    if y[0] > x[0] and y[1] < x [1]:
                        if y[0] == y[1] :
                            sum+=1
                        else :
                            sum+=0.5
                            
        return int(sum)



f = open('A-small-attempt0(2).in', 'r')

all = []   

case=0

for idx , line in enumerate(f):
    
    
    if idx>0:
        if line.find(' ') > -1:
            n = int(line.partition(' ')[0])
            k = int(line.partition(' ')[2])
            all.append((n,k))
        else:
            if (case>0):
                print 'Case #' + str(case)+': '+ str(RopeInternet.calculate(all))
                all = []
            case +=1
                
print 'Case #' + str(case)+': '+ str(RopeInternet.calculate(all))
    


    