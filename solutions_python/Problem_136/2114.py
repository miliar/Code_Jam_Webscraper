import argparse

def to_int_list(string):
    return [float(x) for x in string.split()]

def get_fastest_time(farm_price, farm_boost, target, current_rate):
    naive_time = 1
    time_with_farm = 0

    time_for_past_farms = 0
    while naive_time > time_with_farm:
        #naive - don't buy farm
        naive_time = target/current_rate + time_for_past_farms

        #first approximation: time to farm + remainder
        farm_time = farm_price/current_rate
        new_rate = current_rate + farm_boost
        target_time = target/new_rate
        time_with_farm = farm_time + target_time + time_for_past_farms

        #print ("naive time: {0}, time after adding a farm: {1} and increasing rate to {2}".format(naive_time,  time_with_farm, new_rate))

        #update variables
        time_for_past_farms = time_for_past_farms + farm_time
        current_rate = new_rate
       
    return round(naive_time,7)

def process_input(filename):
    with open(filename, 'r') as infile:
        T = int(infile.next())
        for i in range(1,T+1):
            C, F, X = to_int_list(infile.next())
            #print 'C: {0}, F: {1}, X: {2}'.format(C,F,X)
            output = get_fastest_time(C, F, X, 2)
            write_output(output, i)


def write_output(output, t):
    print ("Case #{0}: {1}".format(t, output))


#==============================
# Copy below for future programs
#===============================

def main():
    args = arg_parse()
    process_input(args.input_file)


def arg_parse():
    parser = argparse.ArgumentParser(description='Solve the 2014 Google Code Jam Magic Trick problem')
    parser.add_argument('input_file', metavar='file')

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()
