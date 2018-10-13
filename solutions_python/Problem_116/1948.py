import numpy
import re
def won(seq,p):
    if(seq.count(p)==3 and seq.count('T')==1):
        return True
    elif(seq.count(p)==4):
        return True
    else:
        return False

xwon = lambda x: won(x,'X')
owon = lambda x: won(x,'O')

test_cases = int(raw_input())
for i in range(0,test_cases):
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    l1.extend(raw_input())
    l2.extend(raw_input())
    l3.extend(raw_input())
    l4.extend(raw_input())
    a = numpy.array([l1,l2,l3,l4])
    wonby = False
    empty = False
    for j in range(0,4):
        row = a[:,j].tolist()
        col = a[j,:].tolist()
        if(xwon(row) or xwon(col)):
            wonby = "X"
            break
        elif(owon(row) or owon(col)):
            wonby = "O"
            break
        elif(empty==False):
            empty = True if row.count('.')>0 or col.count('.')>0 else False
    if wonby==False:
        dia = a.diagonal().tolist()
        dia2 = numpy.rot90(a).diagonal().tolist()
        if(xwon(dia) or xwon(dia2)):
            wonby = "X"
        elif(owon(dia) or owon(dia2)):
            wonby = "O"
        if wonby==False:
            if empty:
                print "Case #"+str(i+1)+": Game has not completed"
            else:
                print "Case #"+str(i+1)+": Draw"
        else:
            print "Case #"+str(i+1)+": "+wonby+" won"
    else:
        print "Case #"+str(i+1)+": "+wonby+" won"
    if i!=test_cases-1:
        raw_input()
