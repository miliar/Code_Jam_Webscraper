def get_num(motes, new_size):
    size = new_size
    count = 0
    while motes != []:
        if motes[0] < size:
            size = size + motes[0]
            motes.pop(0)
        else:
            popd = False
            for i in range(len(motes)):
                #print('for : '+str(i))
                if motes[0] < (size+size-1):
                    size = size + size + motes[0] - 1
                    count = count + 1
                    motes.pop(0)
                    popd = True
                    break
                else:
                    #print('came')
                    size = size + size - 1
                    count = count + 1

            if popd == False:
                return 1000

    return count

    
f = open('A-large.in', 'r')
#f = open('practice.txt', 'r')

output = open('output1.txt','w')

T = int(f.readline())

#print(T)

for i in range(1,T+1):
    line1 = f.readline().rstrip().split()
    motes = [int(x) for x in f.readline().rstrip().split()]

    size = int(line1[0])

    motes.sort()

    result = 0

    while motes != []:
        if motes[0] < size:
            size = size + motes[0]
            motes.pop(0)
        else:
            if motes[0] < (size+size-1):
                size = size + size + motes[0] - 1
                result = result + 1
                motes.pop(0)
            else:
                max_size = result + len(motes)
                k = get_num(motes, size)
                motes = []
                if (k < max_size):
                    result = result + k
                else:
                    result = max_size

        #print (motes[0])

    text = 'Case #'+str(i)+': '+ str(result)

    print(text,file=output)
    #print(text)

    #print()

f.close()
output.close()

#print(lines)
