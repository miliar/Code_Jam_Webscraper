infile = open('D:\study\codejam\codejam2014\A-small-attempt0.in','r')
outfile = open('D:\study\codejam\codejam2014\A-small-attempt0.out','w')
def main():
    T = int(infile.readline())
    for case in range(1,T+1):
        doCase(case)
    infile.close()
    outfile.close()

def doCase(case):
    m = int(infile.readline())
    for i in range(1,5):
        if i == m:
            set1 = [int(x) for x in infile.readline().split()]
        else:
            infile.readline()
    n = int(infile.readline())
    for i in range(1,5):
        if i == n:
            set2 = [int(x) for x in infile.readline().split()]
        else:
            infile.readline()
    outfile.write('Case #'+str(case)+': '+check(set1,set2)+'\n')
    #print('case #'+str(case)+' '+check(set1,set2))    

def check(set1,set2):
    card = [val for val in set1 if val in set(set2)]
    if len(card) == 1:
        result = str(card[0])
    elif len(card) >1:
        result = 'Bad magician!'
    else:
        result = 'Volunteer cheated!'
    return result
