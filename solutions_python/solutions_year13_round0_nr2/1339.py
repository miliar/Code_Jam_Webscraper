import copy
f = open('ad.in','r')
totalCases = int(f.readline().strip())
f2=open('out','w')

def getMax(matrix,y):
    highest=-1
    for q in range(0,len(matrix)):
        if matrix[q][y]>highest:
            highest=matrix[q][y]
    return highest
for i in range(0,totalCases):
    print "Case #%d:" % (i+1),
    f2.write("Case #%d: " % (i+1))
    x,y = [int(a) for a in f.readline().strip().split(' ')]
    matrix = []
    for rmamsd in range(0,x):
        matrix.append([int(a) for a in f.readline().strip().split(' ')])
    marker = copy.deepcopy(matrix)
    for p in range(0,x):
        for q in range(0,y):
            marker[p][q]=0
    for p in range(0,x):
        maximum = max(matrix[p])
        for q in range(0,y):            
            if matrix[p][q]!=maximum:
                marker[p][q]=1
    try:
        for p in range(0,y):
            maximum = getMax(matrix,p)
            for q in range(0,x):
                if matrix[q][p]!=maximum and marker[q][p]:
                    raise Exception
        print "YES"
        f2.write("YES\n")
    except Exception,e:
        print "NO"
        f2.write("NO\n")
f2.close()
