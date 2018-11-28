def min(a,b):
    if a < b :
        return a
    else :
        return b
        
def min_l(l):
    minimum = l[0]
    for e in l :
        minimum = min(e,minimum)
    return minimum
    
    
def max(a,b):
    if a > b :
        return a
    else :
        return b
        
def max_l(l):
    maximum = l[0]
    for e in l :
        maximum = max(e,maximum)
    return maximum
    
def last_tidy(str_n):
    l_n = []
    for char in str_n :
        if char.isdigit():
            l_n.append(int(char))
            
    flag = False #flag repère si on a déjà fait une substitution
    i = 1
    i_nb = 0
    nb_i = l_n[0]
    flag = False
    while i < len(l_n) and not flag:
        if l_n[i] == nb_i :
            i += 1
        else :
            if l_n[i] < l_n[i-1]:
                l_n[i_nb] -= 1
                flag = True
                break
            else :
                nb_i = l_n[i]
                i_nb = i
                i += 1
    if flag :
        for i in range(i_nb + 1, len(l_n)):
            l_n[i] = 9

    str_sol = ""
    for e in l_n :
        str_sol = str_sol + str(e)
    if str_sol[0] == '0' :
        return(str_sol[1:])
    else :
        return(str_sol)



import os

os.chdir('C:/Users/Noé/Documents/projet info/python/codejam')

file_test = open('B-large.in','r')
file_solution = open('solution_tidy.txt','w')


id_case = 1 
nb_case = int(file_test.readline())
print(nb_case)


for line in file_test :
    pb_input = str(int(line))
    pb_output = last_tidy(line)
    print(pb_output)
    file_solution.write("Case #{}: {}\n".format(str(id_case), str(pb_output)))
    id_case += 1
    
file_test.close()
file_solution.close()
