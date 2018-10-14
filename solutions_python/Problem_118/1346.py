#Tom Dobrow
#Google Code Jam, Round 1, Problem 1
#4-13-2013

#1, 4, 9, 121, 484

def read_words(afile):
    words = []
    for line in afile:
            words.append(line.strip())
    return words


def Check(x, y):
    value = 0
    z = int(x)
    q = int(y)
    if ((z<=1) and (q>=1)):
        value += 1
    if ((z<=4) and (q>=4)):
        value += 1
    if ((z<=9) and (q>=9)):
        value += 1
    if ((z<=121) and (q>=121)):
        value += 1
    if ((z<=484) and (q>=484)):
        value += 1

    return value
    
    


filename = open('Tim.txt' , 'r')
T = filename.readline()
alist = read_words(filename)
for i in range (int(T)):
    s = alist[i].split()
    a = s[0]
    b = s[1]
    NumberOfAnswers = Check(a,b)
    print 'Case #' + str(i+1) + ': ' + str(NumberOfAnswers)
    
filename.close()