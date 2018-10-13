
#reading file
with open("A-large.in") as z:
    casen = int(z.readline())
    
    #case!
    for case in range(1,casen+1):

        #reading file
        data = z.readline().strip().split(" ")

        #defining variables
        size = int(data[1])
        sequence = data[0]
        length = len(sequence)


        #greedy works. 

        #firstly, check if impossible
        def f(x,y):
            yans = 0
            for a2 in range(0,len(y)):
                if y[a2]=="-":
                    yans=1
            
            if yans==0:
                return 0
            elif x==length-size:
                return 1
            else:
                return 2
        moves = 0
        position = -1
        while f(position, sequence)==2: #flipper still works and sequence not finished
            position+=1
            if sequence[position]=="-":
                moves+=1
                for a3 in range(position, position+size):
                    if sequence[a3]=="+":
                        sequence = sequence[:a3]+"-"+sequence[a3+1:]
                    elif sequence[a3]=="-":
                        sequence = sequence[:a3]+"+"+sequence[a3+1:]
        if f(position,sequence)==0:
            print("Case #"+str(case)+": "+ str(moves))
        elif f(position,sequence)==1:
            print("Case #"+str(case)+": "+ "IMPOSSIBLE")
