import glob

def processquestion(index, n,m, question):
    print "Case #%d:"%index,
    #iff an element is not lower than both the maximum in the column and the maximum in the row, only then it is possible
    #if all elements are possible, the field is possible

    for i in xrange(n):
        for j in xrange(m):
            maximi = -1
            for ind in xrange(n):
                if maximi < question[ind][j]:
                    maximi = question[ind][j]
            maximj = -1
            for ind in xrange(m):
                if maximj < question[i][ind]:
                    maximj = question[i][ind]
            if question[i][j] < maximi and question[i][j] < maximj:
                print "NO"
                return
    print "YES"
            
with open(glob.glob('*.in')[0]) as p:
    numquestions = int(p.readline().strip())
    
    for questionindex in xrange(numquestions):
        question = ''
        line = p.readline().strip()
        a,b = line.split(' ')
        n = int(a)
        m = int(b)
        question = []
        for lineindex in xrange(n):
            elems = p.readline().strip().split(' ')
            list = []
            for el in elems:
                list.append(int(el))
            question.append(list)
            
        processquestion(1+questionindex, n,m, question)
    
    