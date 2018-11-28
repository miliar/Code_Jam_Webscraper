import os

#dealing with reading
folder = os.path.dirname(__file__)
text_files = [f for f in os.listdir(folder)]
#print text_files
filename = u'B-large.in'

text_file = open(folder+"/"+filename, "r")

input = []
for line in text_file:  # opened in text-mode; all EOLs are converted to '\n'
    line = line.rstrip('\n')
    input.append(line)    
#print input

#dealing with writing
output = u'B-large.out'
out = open(folder+"/"+output,'w')


#specifici problem
tt = int(input[0])
#print tt


for x in xrange(tt):
    paths = []
    #print "testcase#" + str(x) + ":" 
    case = input[x+1].split()
    #print case
    C = float(case[0])
    F = float(case[1])
    X = float(case[2])
    #print "C:" + case[0]
    #print "F:" + case[1]
    #print "X:" + case[2]
    #rows order: C's, rate per second, X, time to next C, total time until next C, time to X witn no extra C
    #init case:
    rate = 2.0
    paths.append([0, rate, X, C/rate, C/rate, X/rate])
    rate += F
    n=0
    #print paths[n][5]
    #print paths[n][4] + X/rate
    
  
    while(paths[n][4] + X/rate < paths[n][5]):
        paths.append([n+1, rate, X, C/rate, paths[n][4] + C/rate, paths[n][4] + X/rate])
        rate += F
        n += 1    
    #print paths
    #print "Result:" + str(paths[n][5])
    #print "Case #" + str(x+1) + ": " + str(round(paths[n][5],7))
    #print "Case #" + str(x+1) + ": " + '{0:.7f}'.format(paths[n][5])
    out.write("Case #" + str(x+1) + ": " + '{0:.7f}'.format(paths[n][5]) + "\n")
    #print "----"
    
text_file.close()
out.close()