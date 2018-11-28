import math
import sys
import getopt

def get_arguments():
    in_file= "/home/se/Downloads/A-small.in"
    out_file ="/home/se/Downloads/test.out"
    opts, args = getopt.getopt(sys.argv[1:], "i:o:")
    for o, a in opts:
        print o
        if o in ("-i"):
            in_file = a;
        elif o in ("-o"):
            out_file = a;
    print(in_file, out_file)
    return (in_file, out_file)

def run(in_file, out_file):
    input = open(in_file)
    output = open(out_file, "w")

    line = input.readline().strip()
    cases = int(line)

    for case in range(0,cases):
        (farm_cost, farm_rate, target) = get_details(input.readline().strip())
        answer = optimum_cookie_strategy(farm_cost, farm_rate, target)
        print >> output, "Case #%d: %.7f" % (case+1, answer)
        print "Case #%d: %.7f" % (case+1, answer)

def get_details(details_line):
    details = details_line.split(' ')
    farm_cost = float(details[0])
    farm_rate = float(details[1])
    target =    float(details[2])
    return (farm_cost, farm_rate, target)

def optimum_cookie_strategy(farm_cost, farm_rate, target):
    #print "Farm Cost "+str(farm_cost)
    #print "Farm Rate "+str(farm_rate)
    #print "Target "+str(target)
    base_rate = 2.0;
    previous_best_time = target/base_rate
    #print "Previous Best Time"+str(previous_best_time)
    rate = 2.0;
    time = 0;
    while(True):
        time_to_next_farm = (farm_cost/rate);
        #print "To next farm "+str(time_to_next_farm)
        time_to_target = time+time_to_next_farm+target/(rate+farm_rate)
        #print "Time to target "+str(time_to_target)
        if (time_to_target > previous_best_time):
            return previous_best_time
        else:
            rate+=farm_rate;
            time+=time_to_next_farm
            previous_best_time = time_to_target

def main():
    (in_file, out_file) = get_arguments()
    run(in_file, out_file)

main()

