def check_tidy(n):
    str_n = str(n)
    is_tidy = True
    index = 0
    #maxlim = len(str_n)
    while(is_tidy and index < len(str_n) - 1 ):
        #print(index)
        is_tidy = str_n[index] <= str_n[index+1]
        index += 1
    return(is_tidy)

def fix_num(n):
    while (not check_tidy(n)):
        list_n = list(str(n))
        changed = False
        index = 0
        while (index <  len(list_n) - 1):
            if (changed == True):
                list_n[index] = '9'
                list_n[index + 1] = "9"
            if(changed == False and list_n[index] > list_n[index + 1]):
                list_n[index] = str(int(list_n[index]) - 1)
                list_n[index + 1 ] = '9'
                changed = True
            index += 1
        n = int("".join(list_n))
    return(n)

file = open("B-large.in", 'r')
out = open("out.txt", 'w')
#num_prob = int(input())
num_prob = int(file.readline())
#for i in range (1, num_prob + 1):
i = 0
for line in file:
    i += 1
    #print(line)
    num = int(line) 
    #num = int(input())
    num = fix_num(num)
    #print(num)
    val = "Case #{}: {}\n".format(i,num)
    #print(val)
    out.write(val)
file.close()
out.close()
