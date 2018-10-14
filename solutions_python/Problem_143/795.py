import os

#dealing with reading
folder = os.path.dirname(__file__)
text_files = [f for f in os.listdir(folder) ]
print text_files
filename = u'B-small-attempt0.in'


text_file = open(folder+"/"+filename, "r")

input = []
for line in text_file:  # opened in text-mode; all EOLs are converted to '\n'
    line = line.rstrip('\n')
    input.append(line)    
print input

#dealing with writing
output = u'B-small-attempt0.out'
out = open(folder+"/"+output,'w')


#specifici problem
tt = int(input[0]) + 1
#print tt

for x in xrange(1,tt):
    inp = [int(i) for i in input[x].split()]
    #print inp
    p = 0
    a = inp[0]
    b = inp[1]
    K = inp[2]
    for A in range(0, a):
        for B in range(0, b):
            op = A&B
            #print "<" + str(A) + "," + str(B) + ">" + "=" + str(op)
            if op < K:
                p += 1

    print p
    out.write("Case #" + str(x) + ": " + str(p) +  "\n")

text_file.close()
out.close()