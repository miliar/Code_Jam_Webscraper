import math

file_name='C-small.in'

infile = file(file_name,'r')
no_of_test = infile.readline().strip()
result = ''


print 'I am thinking...'

def palindrome(n):
    #print 'n', n
    LHS = str(n)
    #print 'LHS', LHS

    RHS = LHS[::-1]
    RHS = RHS.lstrip('0')
    #print 'RHS', RHS

    return LHS==RHS


def fair_n_square(n):
    x = math.sqrt(n)
    if n%x==0:
        return palindrome(int(x)) and palindrome(n)
    return False


for i in range(1,int(no_of_test)+1):
    cnt=0
    lst = infile.readline().split()
    #print lst
    for n in range(int(lst[0]),int(lst[1])+1):
        # if n**2 in range(int(lst[0]),int(lst[1])+1) and
        if fair_n_square(n):
             cnt = cnt + 1
    result = result + 'Case #'+str(i)+': ' + str(cnt)+'\n'

infile.close()

print 'Write to file now...'

outfile = file(file_name[:file_name.find('.')]+'.out', 'w')
outfile.write(result)
outfile.close()

print 'Write to file is done.'



            
    
