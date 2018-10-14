#Candy Splitting Google Code Jam Problem
# by Sean Egan

total_candies = []
value_array = []
value_double_array = []
split_array = []
split_double_array = []
i = 0
file_ = open('C-small-attempt0.txt','r')
for line in file_:
    i = i + 1
    if (i == 1):
        total_cases = int(line)
    else:
        if(i % 2 == 1):
            split_line = line.split(' ')
            for x in range(0,len(split_line)):
                value_array.append(int(split_line[x]))
                split_array.append(0)
            value_double_array.append(value_array)
            split_double_array.append(split_array)
            value_array = []
            split_array = []
        elif(i % 2 == 0):
            total_candies.append(int(line))

for x in range(0,total_cases):
        solution = -1
        total_combos = 2**len(split_double_array[x])
        for y in range(0,total_combos):
            pats_sum0 = 0 #The sums Patrick has for each pile
            pats_sum1 = 0
            any_amount0 = False
            any_amount1 = False
            seans_sum0 = 0 #The sums Sean has for each pile
            seans_sum1 = 0
            for z in range(0, len(split_double_array[x])):
                if(y/(2**z) % 2 == 0):
                    split_double_array[x][z] = 0
                else:
                    split_double_array[x][z] = 1
            for z in range(0, len(value_double_array[x])):
                if(split_double_array[x][z] == 0):
                    pats_sum0 = pats_sum0 ^ value_double_array[x][z]
                    seans_sum0 = seans_sum0 + value_double_array[x][z]
                    any_amount0 = True
                else:
                    pats_sum1 = pats_sum1 ^ value_double_array[x][z]
                    seans_sum1 = seans_sum1 + value_double_array[x][z]
                    any_amount1 = True
            if(pats_sum0 == pats_sum1 and any_amount0 and any_amount1):
                if(seans_sum0 > solution):
                    solution = seans_sum0
                if(seans_sum1 > solution):
                    solution = seans_sum1

        if(solution == -1):
            print "Case #{0}: NO" .format(x+1)
        else:
            print "Case #{0}: {1}" .format(x+1,solution)
