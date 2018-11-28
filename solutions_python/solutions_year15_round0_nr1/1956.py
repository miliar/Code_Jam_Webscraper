def get_num_friends(case_num, line, out):
    print(line)
    [max_shyness, sequence] = line.split()
    max_shyness = int(max_shyness)
    friends = 0
    num_standing = 0
    for shyness in range(0, max_shyness + 1):
        if (num_standing > shyness):
            num_standing += int(sequence[shyness])
        else:
            more_friends = (shyness - (num_standing)) 
            friends += more_friends
            num_standing += more_friends + int(sequence[shyness])
    
    print "Num " + str(friends)
    out.write("Case #" + str(case_num) + ": " + str(friends) + "\n")
        
if __name__ == "__main__": 

    with open('A-large.in', 'r') as f:
        input = f.readlines()
        
    num_cases = int(input[0])
    
    with open('output.txt', 'w') as out:
        for i in range(1, 1+num_cases):
            get_num_friends(i, input[i], out)
        
