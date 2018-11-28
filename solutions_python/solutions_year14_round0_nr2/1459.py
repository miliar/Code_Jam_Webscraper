#input read
input_file = open("input1.in", 'rt')
num_cases = int(input_file.readline())

#output write
output_file = open("output1.txt", 'w')

# do the job
def main_job(c, f, x):
    v = 2
    time = 0
    while ((x-c)/v) > (x/(v+f)):
        #Buy Farm
        time = time + c/v
        v = v + f
    time = time + x/v
    return time

for i in range(num_cases):    
    print str(i+1) +  "/" + str(num_cases)
    line = input_file.readline().split()
    C = float(line[0])
    F = float(line[1])
    X = float(line[2])
    time = main_job(C, F, X)
    output = "Case #%d: %.7f \n" %(i+1, time)
    output_file.write(output)
    
    
input_file.close()
output_file.close()