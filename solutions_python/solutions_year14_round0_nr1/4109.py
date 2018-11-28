from itertools import product

with open ("/Users/byungchulin/Desktop/A-small-attempt0.in.txt") as f:
    data = f.read()

fd = open("/Users/byungchulin/Desktop/out.txt", 'w')

first_spt = data.split('\n')
case = first_spt.pop(0)

fst_arr = []
snd_arr = []
trd_arr = []
fth_arr = []

fst_arr2 = []

fst_temp_arr = []
snd_temp_arr = []
num = 0
num2 = 0
count = 0
ou= 0

for ccc in range(int(0), int(case)):
    first_guess = first_spt.pop(0) # get the first guess        
#    print(first_guess)
    if( int(first_guess) == 1):
        num = 0

    if( int(first_guess) == 2):
        num = 4

    if( int(first_guess) == 3):
        num = 8

    if( int(first_guess) == 4):
        num = 12
    
    for y in range(int(0), int(4)):
        temp = first_spt.pop(0)
        fst_temp_arr.append(temp.split(' '))
 #   print(fst_temp_arr)
        
    second_guess = first_spt.pop(0) # get the second guess
#    print(second_guess)
    if( int(second_guess) == 1):
        num2 = 0

    if( int(second_guess) == 2):
        num2 = 4

    if( int(second_guess) == 3):
        num2 = 8

    if( int(second_guess) == 4):
        num2 = 12
    
    for z in range(int(0), int(4)):
        temp = first_spt.pop(0)
        snd_temp_arr.append(temp.split(' '))
   # print(snd_temp_arr)

    for f in range (int(0), int(4)):
        fst_arr.append(fst_temp_arr[0][f])

    for f in range(int(0), int(4)):
        fst_arr.append(fst_temp_arr[1][f])

    for f in range(int(0), int(4)):
        fst_arr.append(fst_temp_arr[2][f])

    for f in range(int(0), int(4)):
        fst_arr.append(fst_temp_arr[3][f])

#    print(fst_arr)

    for f in range (int(0), int(4)):
        fst_arr2.append(snd_temp_arr[0][f])

    for f in range(int(0), int(4)):
        fst_arr2.append(snd_temp_arr[1][f])

    for f in range(int(0), int(4)):
        fst_arr2.append(snd_temp_arr[2][f])

    for f in range(int(0), int(4)):
        fst_arr2.append(snd_temp_arr[3][f])    

#    print(fst_arr2)
    
#    print(int(num))
#    print (int(num2))

    a = int(num+4)
    b = int(num2+4)
    
    for x in range( num, int(a)):
        for y in range(num2, int(b)):
            if ( int(fst_arr[int(x)]) == int(fst_arr2[int(y)])):
 #               print(str(fst_arr[int(x)])+" "+str(fst_arr2[int(y)]))
                count = count+1
                if( int(count) == 1):
                    ou = fst_arr[int(x)]
        

    print(ou)
    
    if ( int(count) == 0):
        print("Case #"+str(int(ccc+1))+": Volunteer cheated!", file = fd)

    if( int(count) == 1):
        print("Case #"+str(int(ccc+1))+": "+str(int(ou))+"", file = fd)

    if( int(count) > 1):
        print("Case #"+str(int(ccc+1))+": "+"Bad magician!", file = fd)

    fst_arr = []
    fst_arr2 = []
    fst_temp_arr=[]
    snd_temp_arr=[]
    count = 0
    ou = 0


fd.close()




