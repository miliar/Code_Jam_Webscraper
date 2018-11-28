f = open('Google New Lottery Game Small.in','r')
g = open('Google New Lottery Game Small.out','w')
d = {}
for i in range(1001):
    for j in range(1001):
        d[(i,j)] = i&j

    
def count_winners(A,B,K):
    global d
    count = 0
    for i in range(A):
        for j in range(B):
            if d[(i,j)] < K:
                count += 1
    return count

def Google_print(filename,answers):
    for i in range(len(answers)):
        filename.write("Case #%s: %s\n" % (str(i+1),answers[i]))
        print "Case #%s: %s" % (str(i+1),answers[i])
    return

cases = int(f.readline())
answers = []
for i in range(cases):
    A,B,K = f.readline().rstrip().split(' ')
    A = int(A)
    B = int(B)
    K = int(K)
    answers.append(count_winners(A,B,K))
Google_print(g,answers)
f.close()
g.close()
                   
