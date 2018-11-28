import math

file = open("/Users/Tom/Desktop/c-small-attempt0.in", "r")
lines = file.readlines()
input =[]
for x in lines:
    if len(x.split())>1:
        input.append(x.split())

file.close()


case = 0
text_file = open("/Users/Tom/Desktop/c-small-output.txt", "w")
for x in input:
    start = x[0]
    end = x[1]
    data = [x for x in range(int(start), int(end)+1)]
    sqr_root_eligable = [x for x in data if math.sqrt(x)%1 ==0 or x==1]
    palin_eligable = [x for x in sqr_root_eligable if str(x)== str(x)[::-1]]
    sqr_root = [str(int(math.sqrt(x))) for x in palin_eligable]
    final = [x for x in sqr_root if x == x[::-1]]
    case +=1
    
    text_file.write('Case #%s: %s \n' %(str(case), str(len(final))))
text_file.close()
    
    
    

