'''
Created on May 12, 2013

@author: Federico Raue
'''

def has_vowels(sub_name):
    if len(sub_name) == 0:
        return False
    vowels = "aeiuo"
    for c in sub_name:
        if c in vowels:
            return True
    return False

def get_index(name, start_index, n):
    if start_index >= len(name):
        return -1
    vowels = "aeiuo"
    for index in range(start_index, len(name)):
        if name[index] not in vowels:
            if has_vowels(name[index:index+n]) == False and len(name[index:index+n])==n:
                return index
    return -1
lst_number = [line.strip() for line in open('A-small-attempt0.in', "r")]
file_solution = open('result.txt', 'w')
number_test = int(lst_number.pop(0))


for number_case in range(1, number_test + 1):
    name, n = lst_number.pop(0).split()
    n = int(n)
    n_value = 0
    index_consonant = get_index(name, 0, n)
    lst_result = set([])
    while(index_consonant != -1):
        lst_result.add((index_consonant, name[index_consonant: index_consonant+n]))
        for i in range(index_consonant-1, -1, -1):
            lst_result.add((i, name[i:index_consonant] + name[index_consonant: index_consonant+n]))
            for j in range(index_consonant+n, len(name)+1):
                lst_result.add((i, name[i:index_consonant] + name[index_consonant: index_consonant+n]+ name[index_consonant+n:j]))

        for i in range(index_consonant+n, len(name)+1):
            lst_result.add((index_consonant, name[index_consonant: index_consonant+n] + name[index_consonant+n:i]))
            

        index_consonant = get_index(name, index_consonant+1, n)
    solution = "Case #%d: %d"%(number_case, len(lst_result))
    print solution
    file_solution.write(solution + "\n")
file_solution.close()