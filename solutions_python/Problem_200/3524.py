#open file
f = open('testfile.txt','r')

T = f.readline()
for iter in range(int(T)):
    input = list(f.readline())
    last = 0
    #check if the curret iteration is the last line, contains a newline...
    if input[len(input)-1] != '\n':
        last = 1
    nines = len(input) - 2 + last
    #idea is to read from most sig digit and if there is an untidy digit
    #then everything afterwards will be a nine in the output...
    notDone = True
    while notDone:
        notDone = False
        for i in range(nines):
            if input[i] > input[i+1]:
                input[i] = chr(ord(input[i])-1)
                nines = i
                notDone = True
                break;
    for i in range(len(input)-2+last,nines,-1):
        input[i] = '9'
    numOfZero = 0
    for i in range(len(input)):
        if input[i] == '0':
            numOfZero += 1
        else:
            break;
    output = ''.join(input[numOfZero:len(input) - 1 + last])
    print("Case #{}: {}".format(iter+1,output))
    