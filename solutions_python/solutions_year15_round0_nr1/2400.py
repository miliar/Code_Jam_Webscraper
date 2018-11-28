
try:
    fin = open("A-large.in.txt",'r')
    fout = open("output.txt",'w')
except:
    print('Invalid file names')

cases = int(fin.readline())
for i in range(cases):
    cum_sum = 0;
    num_needed = 0;
    case_line = fin.readline().rstrip().split()
    S_max = int(case_line[0])
    S_string = case_line[1]
    for k in range(S_max+1):
        if k > cum_sum: #not enough less shy audience members
            num_needed += k - cum_sum
            cum_sum += int(S_string[k])+ (k - cum_sum)      #calculate the new cumlative sum with num in audience with that shyness level plus number added
        else: #there were already enough less shy audience members
            cum_sum += int(S_string[k]) #add number of audience members with a shyness of k to the cum sum
    fout.write("Case #" + str(i+1) + ": " + str(num_needed) + "\n")
fin.close()
fout.close()

    
