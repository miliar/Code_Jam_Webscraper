import os.path
import sys

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
filepath = os.path.abspath(os.path.join(__location__, "A-small-attempt0.in"))
f = open(filepath, "r")
filepath = os.path.abspath(os.path.join(__location__, "out.txt"))
fo = open(filepath, 'w')

T=int(f.readline())

for Case in range(0,T):
    L1=int(f.readline())
    for cnt in range(1,L1):
        f.readline()
    NumStr=f.readline()
    list1=NumStr.split()
    for cnt in range(L1,4):
        f.readline()
        
    L2=int(f.readline())
    for cnt in range(1,L2):
        f.readline()
    NumStr=f.readline()
    list2=NumStr.split()
    for cnt in range(L2,4):
        f.readline()
    
    rslt=set(list2) & set(list1)
    
    if (len(rslt)==0):
        fo.write ("Case #" + str(Case+1) + ": Volunteer cheated!\n")
    elif len(rslt)>1:
        fo.write ("Case #" + str(Case+1) + ": Bad magician!\n")
    elif len(rslt)==1:
        fo.write ("Case #" + str(Case+1) + ": " + next(iter(rslt)) + "\n")

f.close()
fo.close()