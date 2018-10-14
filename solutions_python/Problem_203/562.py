f = open("2A-large.in")
o = open("output2AL.txt","w")
no_of_cases = f.readline()
from math import log 
def check_inc(num):
    no = list(str(num))
    for i in range(len(no)-1):
        if no[i]>no[i+1]:
            return int(''.join(no[i+1:]))+1
    return 0

def B():
    for i in range(int(no_of_cases)):
        number = int(f.readline())
        no = 1
        while no:
            no = check_inc(number)
            number -= no
        o.write("Case #"+str(i+1)+": "+str(number)+"\n")
    
def A():
    for i in range(int(no_of_cases)):
        input = f.readline()
        s,k = input.split()
        s = list(s)
        k = int(k)
        bin = [0 if x=='-' else 1 for x in s]
        count = 0
        for j in range(len(bin)-k+1):
            if not bin[j]:
                for x in range(k):
                    bin[j+x] ^= 1
                    count+=1
        if len(set(bin)) == 1 and set(bin)=={1}:
            o.write("Case #"+str(i+1)+": "+str(count//k)+"\n")
        else:
            o.write("Case #"+str(i+1)+": IMPOSSIBLE\n")

#A()
def deng():
    for i in range(int(no_of_cases)):
        input = f.readline()
        total_bth,no_of_ind = input.split()
        total_bth = int(total_bth)
        no_of_ind = int(no_of_ind)
        level = int(log(no_of_ind,2))+1
        if total_bth%2:
            o.write("Case #"+str(i+1)+": "+str((total_bth//(pow(2,level)))-1)+" "+str(total_bth//pow(2,level))+"\n")
        else:
            if no_of_ind == 2^(level)-1:
                level+=1
            o.write("Case #"+str(i+1)+": "+str((total_bth//pow(2,level))-1)+" "+str(total_bth//pow(2,level))+"\n")

#deng()

def fill_the_row(temp,i,j, char):
    for x in range(i,j+1):
        temp[x] = char

def cake():
    for case in range(int(no_of_cases)):
        input = f.readline()
        rows,columns = input.split()
        rows = int(rows)
        columns = int(columns)
        input_mat = []
        result = []
        for i in range(rows):
            temp = ['*' for _ in range(columns)]
            row = f.readline()
            char_tofill = None
            j_tofill = -1
            for j in range(columns):
                if row[j] != '?':
                    temp[j] = row[j]
                    if j_tofill == -1:
                        char_tofill = row[j]
                    else:
                        char_tofill = row[j]
                        fill_the_row(temp,j_tofill,j, char_tofill)
                        j_tofill = -1
                elif j_tofill == -1:
                    j_tofill = j
            if j_tofill != -1:
                if char_tofill == None:
                    if i>0:
                        result.append([x for x in result[i-1]])
                        continue
                else:
                    fill_the_row(temp,j_tofill,j,char_tofill)
            result.append(temp)
        if result[0][0] =='*':
            for result_i in range(rows):
                if result[result_i][0]!='*':
                    break
            for result_1 in range(result_i):
                result[result_1] = [x for x in result[result_i]]

        o.write("Case #"+str(case+1)+":\n")
        for x in range(rows):
            o.write(''.join(result[x]))
            o.write('\n')

cake()