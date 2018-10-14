


"""
INPUT
num of test cases
row chosen
input 1
row chosen
input 2
"""
fd = open("A-small-attempt0.in","r")

lines = fd.readlines()

T = int(lines[0])
if (T < 1) or (T > 100):
    print("Invalid T value: " + lines[0])
    close();

pos = 1;
for prob_num in range(T):
    print("Case #" + str(prob_num+1) + ": ",end="")
    
    guess1 = int(lines[pos])
    line1 = lines[pos + guess1].strip('\n');
    pos += 5;
    guess2 = int(lines[pos])
    line2 = lines[pos + guess2].strip('\n');
    pos += 5;
    
    line1_split = line1.split(' ');
    line2_split = line2.split(' ');

    #test for unique number
    hit_count = 0;
    saved_hit = 0;
    for i in range(4):
        if line1_split[i] in line2_split:
            saved_hit = line1_split[i];
            #print("HIT: " + str(line1_split[i]) + "\t" + str(line2_split));
            hit_count += 1;

    if hit_count > 1:
        print("Bad magician!");
    elif hit_count == 1:
        print(saved_hit)
    else:
        print("Volunteer cheated!");
    

fd.close()
