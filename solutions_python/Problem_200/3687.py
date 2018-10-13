lines = [int(line.rstrip('\n')) for line in open('B-small-attempt0.in')]

str_temp = ''

def last_tidy_number(n):
    for i in range(n,0,-1):
        temp_list = [int(char) for char in str(i)]
        if len(temp_list) == 1:
            return i
        flag = True
        for j in range(len(temp_list)-1):
            if temp_list[j] > temp_list[j+1]:
                flag = False
        if flag == True:
            return i

T = lines[0]
for t in range(1,T+1):
    if t == T:
        str_temp = str_temp+'Case #'+str(t)+': '+str(last_tidy_number(lines[t]))
    else:
        str_temp = str_temp+'Case #'+str(t)+': '+str(last_tidy_number(lines[t]))+'\n'
print(str_temp)
f = open('out.txt', 'w')
f.write(str_temp)
f.close()