f = open('q1file.in' , 'r')
amount = int(f.readline())

def parse_result(caseno , intersection):
    if len(intersection) == 1:
        print "Case #" + str(caseno) + ":",intersection[0]
    if len(intersection) == 0:
        print "Case #" + str(caseno) + ":","Volunteer cheated!"
    if len(intersection) > 1:
        print "Case #" + str(caseno) + ":","Bad magician!"

for i in xrange(0 , amount):
    l1 = []
    l2 = []
    g = int(f.readline())
    for j in xrange(1 , 5):
        line=f.readline()
        if j == g:
            l1=line.split()
    g = int(f.readline())
    for j in xrange(1 , 5):
        line=f.readline()
        if j == g:
            l2=line.split()
    intersection = list(set(l1) & set(l2))
    parse_result(i+1 , intersection)
