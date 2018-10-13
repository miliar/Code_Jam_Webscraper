
import sys
from decimal import *

def main():

    #  reading in the arguments of the code executable
    fin_name = sys.argv[1]
    fout_name = sys.argv[2]

    # opening the output file for writing
    fout = open(fout_name, 'w')

    #  reading all lines at once from the opened file
    with open(fin_name, 'r') as fin:
        lines = fin.readlines()

    # T - number of test casess
    T = int(lines[0].split()[0])
    line_ind = 0

    for test_case in range(1, T+1):
        line_ind += 1
        destination, horses = [int(x) for x in lines[line_ind].split()]
        all_starts_speeds = []

        for horse in range(horses):
            line_ind += 1
            start, speed = [float(x) for x in lines[line_ind].split()]

            all_starts_speeds.append([start, speed])

        all_starts_speeds = sorted(all_starts_speeds, key=lambda x: x[0])

        times = -10.0

        for start_speed in all_starts_speeds:
            time = Decimal(destination - start_speed[0])/Decimal(start_speed[1])
            if times < 0.0:
                times = time

            else:
                times = max(time, times)


        if test_case == 69:
            print("all_starts_speeds, destination", all_starts_speeds, destination)

        max_speed = "%.12f" % (destination/times)

        fout.write("Case #"+str(test_case)+": "+max_speed[:-6]+"\n")

    fin.close()
    fout.close()

def get_common_start_speed(start_speed, new_start_speed, destination, time_used):


    if new_start_speed[1]-start_speed[1] != 0:
        time = Decimal(start_speed[0]-new_start_speed[0])/Decimal(new_start_speed[1]-start_speed[1])
    else:

        time = 0.0

    if time <= 0.0:
        return [start_speed,time_used]

    else:
        start_speed = [Decimal(start_speed[0]) + time*Decimal(start_speed[1]), min(start_speed[1], new_start_speed[1])]
        return [start_speed, Decimal(time_used) + Decimal(time)]

if __name__ == "__main__":
    main()
