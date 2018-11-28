
def main(input_address):
    input_file = open(input_address, "r")
    output_file = open("D:\\output.txt","w")
    solve(input_file, output_file)
    input_file.close()
    

def solve(input_file, output_file):
    cases = input_file.readline()
    for i in range(int(cases)):
        parameters = input_file.readline().split()
        for t in range(3):
            parameters[t] = float(parameters[t])

        #print parameters

        output_file.write("Case #" +
                          str(i+1) + ": " + str(checkSeconds(parameters, parameters[0],parameters[0]/2)) + "\n")
        #print "\n\n"

def checkSeconds(param, current, time, rate = 2):

#param[0] is the cost of the farm
#param[1] is the addition one farm makes to the rate of cookie-making
#param[2] is the final number of cookies needed
#current is the current number of cookies
#time is the time elapsed until the current point (in seconds)
#rate is the current rate of cookie increase (per second)
    
    #print str(current) + "/" + str(time) + "/" + str(rate)
    while current < param[2]:

        if (param[2]-current) / rate <= (param[2] - current +param[0])/(rate+param[1]):
            current = current+param[0]
            time = time + (param[0]/rate)
        else:
            time = time + (param[0]/(rate+param[1]))
            rate = rate+param[1]

    if current == param[2]:
            return time
    elif current > param[2]:
            return time - ((current - param[2]) / rate)

main("D:\\B-large.in")
