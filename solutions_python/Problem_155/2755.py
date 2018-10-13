# -*- coding:Utf-8 -*-



with open("Input_file.in", 'r') as file:
    content = file.read().splitlines()

with open("Output_file.txt", 'w') as file:
    for k in range(1, int(content[0]) + 1):
        temp = content[k].split()
        Smax, nb_S = int(temp[0]), temp[1]
        nb_needed = 0
        nb_up = 0
        for i in range(Smax + 1):
            if nb_up < i:
                nb_needed += (i - nb_up)
                nb_up = i
            nb_up += int(nb_S[i])
        file.write("Case #" + str(k) + ": " + str(nb_needed) + "\n")
    
    