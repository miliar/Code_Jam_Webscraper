import string

table = string.maketrans("abcdefghijklmnopqrstuvwxyz", "yhesocvxduiglbkrztnwjpfmaq")

n=input()
case=1
while n!=0:
    original = raw_input()
    print 'Case #'+str(case)+": "+original.translate(table)
    case+=1
    n=n-1
