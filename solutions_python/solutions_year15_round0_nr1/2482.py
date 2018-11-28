input_file = "A-large.in"
output_file = "output"
import  sys
if input_file:
    sys.stdin = open(input_file)
    #sys.stdout = open(output_file)

T = input()

for i in range(T):
    line = raw_input()
    line = line.split(' ')

    highest = int(line[0])

    string = line[1]

    amount = 0
    standing = 0
    for d in range (highest+1):
        if(len(string) > d):
           if(standing < d):
               #print amount, standing, d
               if(int(string[d]) > 0):
                   amount += d-standing
                   standing += d-standing
           standing += int(string[d])
           #print amount, standing
    output = "Case #" + str(i+1) + ":"
    print output, amount






