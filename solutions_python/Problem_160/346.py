##from http://stackoverflow.com/questions/147515/least-common-multiple-for-3-or-more-numbers by J.F. Sebastian
def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)


def lcm_all(nums):
    """Return lcm of args."""
    lcms = [lcm(nums[0], nums[1])]
    for ii in range(2, len(nums)):
        lcms.append(lcm(nums[ii], lcms[-1]))
    return lcms
##################################################################################################################

__author__ = 'Zeddy'


if __name__ == "__main__":
    fin = open('B-small-attempt2.in', 'r')
    fout = open('B-small-attempt2', 'w')

    cases = fin.readline()

    for case_num in range(0, int(cases)):
        line = fin.readline().split(' ')
        num_barbers = int(line[0])
        num_customers = int(line[1])

        line = fin.readline().split(' ')

        barbers_times = []
        barber_next_avail = []
        for i in range(0, num_barbers):
            barbers_times.append(int(line[i]))
            barber_next_avail.append(0)

        lcm_list = lcm_all(barbers_times)
        large_lcm = lcm_list[-1]

        lcm_people = 0
        for i in range(0, num_barbers):
            lcm_people += large_lcm/barbers_times[i]

        num_customers = (num_customers-1)%lcm_people
        num_customers +=1

        next_barber = 0
        for i in range(0, num_customers):
            temp_avail_time = barber_next_avail[:]
            temp_avail_time.sort()
            next_time = temp_avail_time[0]
            next_barber = barber_next_avail.index(next_time)
            barber_next_avail[next_barber] += barbers_times[next_barber]

       # mins_passed = 1
#
        print "Case #" + str(case_num+1) + ": " + str(next_barber+1)
        fout.write("Case #" + str(case_num+1) + ": " + str(next_barber+1) + "\n")

    fin.close()
    fout.close()
