input_file = open("a-large-input.txt", "r")
output_file = open("a-large-output.txt", "w")
data = input_file.readlines()
T = int(data[0])
print(T)
for t in range(1, T+1):
    cakes, k = [x for x in data[t].split()]
    k = int(k)
    cakes = list(cakes)
    flips = 0
    impossible = False
    #Algorithm to calculate number of flips needed
    number_of_cakes = len(cakes)
    for i in range(number_of_cakes):
        cake = cakes[i]
        if cake is "+":
            continue
        #Else if we have room to do a flip
        elif i + k <= number_of_cakes:
            flips = flips + 1
            #Do the flip
            for j in range(k):
                if cakes[i+j] == "+":
                    cakes[i+j] = "-"
                else:
                    cakes[i+j] = "+"
        else:
            impossible = True
            break
    #Decide what should be outputted into the file
    if impossible:
        output_file.write("Case #{}: IMPOSSIBLE\n".format(t))
    else:
        output_file.write("Case #{}: {}\n".format(t, flips))
    
input_file.close()
output_file.close()
print("Files closed")
