input_file=open("C:\Users\Lipman\Desktop\input.txt",'r')
output_file=open("C:\Users\Lipman\Desktop\output.txt","w")
cases=int(input_file.readline()[:-1])
for i in xrange(cases):
    case=input_file.readline()[:-1]
    l=case.split(' ')
    l=[int(arg) for arg in l]
    [x,c,r]=l
    if x==1:
        output_file.write("Case #{0}: GABRIEL\n".format(i+1))
    elif x==2 and (c%2==0 or r%2==0):
        output_file.write("Case #{0}: GABRIEL\n".format(i+1))
    elif x==3 and ((c==3 and r>1) or (r==3 and c>1)):
        output_file.write("Case #{0}: GABRIEL\n".format(i+1))
    elif x==4 and ((c>=3 and r==4) or (c==4 and r>=3)):
        output_file.write("Case #{0}: GABRIEL\n".format(i+1))
    else:
        output_file.write("Case #{0}: RICHARD\n".format(i+1))
input_file.close()
output_file.close()
