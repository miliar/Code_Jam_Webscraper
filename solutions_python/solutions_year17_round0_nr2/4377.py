file=open("C:/Users/Vijay/Downloads/B-small-attempt0.in")
content=file.read().split()
tests=int(content[0])
for test in range(tests):
    number=list(content[test+1])
    stack=[]
    for i in range(1,len(number)):
        if number[-i-1]>number[-i]:
            for j in range(i):
                number[-j-1]='9'
            number[-i-1]=chr(ord(number[-i-1])-1)
    new_number=""
    for i in number:
        if i>'0':
            new_number=new_number+i
    print "Case #"+str(test+1)+": "+new_number
file.close()
