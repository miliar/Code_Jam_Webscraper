the_input_file="B-large.in"
the_output_file="tidyNumbers.out"

with open(the_input_file, 'r') as f:
    numbers = [line.rstrip('\n') for line in f]
    
answers=[]

del(numbers[0])

for n in numbers:    
    length=len(n)
    
    if (length==1):
        answers.append(n)
        pass
    
    else:
        j=0
        for i in xrange(length-1):
            if (n[j]!=n[i]):
                    j=i
                    
            if n[i]>n[i+1]:
                if i!=j:
                    i=j
                    
                n=int(n)
                power=10**((length-i)-1)
                n=((n/power)*power)-1
                break
            
        answers.append(str(n))
                
length=len(answers)
 
with open(the_output_file, 'w') as f:
    for i in xrange (length):
        ans="Case #"+str(i+1)+": "+str(answers[i])+'\n'
        print ans
        f.write(ans)

