import math
def palindrome(s):
    return True if str(s) == str(s)[::-1] else False
def is_perfect_square(n):
    if n < 0 :
        return false;
    root= round(math.sqrt(n));
    if palindrome(root):
        return n == root * root;
    else:
        return False
f = open('c.in', 'r')
a=f.readline()
f1=open('output.txt','w')
for x in range(int(a)):
    b=f.readline()
    splitted=b.split();
    lower=splitted[0]
    upper=splitted[1]
    theRefinedList=[]
    for i in range(int(lower),int(upper)+1):
       if (is_perfect_square(i) and palindrome(i)):
           theRefinedList.append(i)
   ## f1.write(str(len(theRefinedList)))
    st=str(len(theRefinedList))
    print("Case #"+str(x+1)+": "+st,file=f1)
    print("----------------------------")

f1.close()
print(palindrome(1))

print(is_perfect_square(1))
