
"""
Given a number N, break it down into an array

N = '999' outputs
a = [[1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1]]
It's just magic
"""
def magic(N):

    bar = []

    for i in range(len(N)):
        bar.append([0]*9)
    for j in range(0,len(N)):
        x = int(N[j])
        for i in range(0,x):
            bar[j][i] = 1
    return bar, len(N)

def help(s): # reduces the order by one decimal, for example 100 to 10
    bar = [0]*9
    if s == 0:
        bar = [1]*9
    else:
        for i in range(0,s-1):
            bar[i]=1
    return bar

def unmagic(bar):
    s = 0
    tidy_N = ""
    tiding_N = ""
    for i in range(0, len(bar)):
        s = sum(bar[i])
        tiding_N += str(s)
    tidy_N = int(tiding_N)
    return tidy_N

def wizard(bar, index):
    aux_bar = bar[:]
    s=0
    flag = 0
    while(flag < index ):
        for i in range(0, index):
            if aux_bar[index-i-1] < aux_bar[index-i-2] and i!=index-1:
                aux_bar[index-i-1] = [1]*9
                aux_bar[index-i-2] = help(sum(bar[index-i-2]))
                flag = 0
            elif aux_bar[index-i-1] >= aux_bar[index-i-2]:
                flag += 1

    return aux_bar


order = []
with open("input.txt") as f:
    file_o = open('output.txt','w') #GET IT OPEN HERE
    input = f.readlines()
    input_x = [i.replace("\n", "") for i in input]
    test_size = int( input_x[0] )

    if test_size == len(input_x[1:]):
        for j in range(0, test_size):
            order.extend(input_x[j+1].split(" "))
        print("test ",order , len(order))
        bar = []
        index = []
        for i in range(0, len(order)): # The input is now ready for some magic
            bar, index = magic(order[i])
            untidy = wizard(bar, index)
            tidy = unmagic(untidy)
            print("tidy", tidy)
            file_o.write("Case #"+ str(i+1) +": "+ str(tidy) +"\n")
    else:
        print ("Input count error")
    file_o.close()
