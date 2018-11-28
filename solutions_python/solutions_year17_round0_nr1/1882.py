def flip(arr):
    flipped=[]
    for i in arr:
        if i=='-':
            flipped.append('+')
        else:
            flipped.append('-')
    # print("Flip: ",arr)
    return flipped

def pancake(arr,k):
    flip_count=0
    for i in range(len(arr)):
        if arr[i] == '-':
            if(len(arr[i:i+k])<k):
                return [arr,'Impossible']
            else:
                temp=flip(arr[i:i+k])
                flip_count=flip_count+1
                arr[i:i+k]=temp
    # print("Pancake: ",arr)
    return [arr,flip_count];
#-------------------------------------------------------------------------------------
i=0
f = open('A-large.in',mode='r')
test = []
for line in f:
    test.append(line)

f = open('large_output_sai.txt', 'w')

for i in range(1,len(test)):
    k=test[i].split(' ')[1]
    arr=test[i].split(' ')[0]
    result = pancake(list(arr),int(k))
    res = "Case #" + str(i) + ": " + str(result[1])+'\n'
    f.write(res)

f.close()
#