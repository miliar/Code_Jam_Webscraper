f = open('A-small-attempt0 (1).in', 'r')
num=int(f.readline())
output=open('result','w')
case=0
def num_of_insert(initial, to_mock):
    num_to_add=0
    while initial<=to_mock:
        initial+=initial-1
        num_to_add+=1
    initial+=to_mock
    return [num_to_add, initial]
while num!=0:
    num-=1
    case+=1
    line=f.readline().split()
    initial_mote=int(line[0])
    amount_motes=int(line[1])
    motes=[int(x) for x in f.readline().split()]
    motes.sort()
    motes_len=len(motes)
    result=[]
    number_of_operations=0
    if initial_mote==1:
        number_of_operations=motes_len
    else:
        for i in range(motes_len):
            if motes[i]<initial_mote:
                initial_mote+=motes[i]
            else:
                result=num_of_insert(initial_mote,motes[i])
                num_to_del=motes_len-i
                if num_to_del > result[0]:
                    initial_mote=result[1]
                    number_of_operations+=result[0]
                else:
                    number_of_operations+=num_to_del
                    break
                    
    print('Case #'+str(case)+': '+str(int(number_of_operations)))
    output.write('Case #'+str(case)+': '+str(int(number_of_operations))+'\n')
output.close()
