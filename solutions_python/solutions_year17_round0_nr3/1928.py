import sys
from sortedcontainers import SortedList
import time

def stall_calculator_fastest(stalls, peeps):
    l = SortedList()
    l.add(stalls)
    peep_dict = {}
    for i in range(0,peeps):
        value = l.pop()    
        longest_int = int(value/2)
        halved = value-longest_int-1
        l.add(longest_int)
        if(halved != 0):
            l.add(halved)
        peep_dict[i]=(longest_int,int((value-1)/2))
    return (longest_int,int((value-1)/2)), peep_dict

def read_in():
    array = []
    for line in sys.stdin.readlines():
        array.append(line.rstrip())

    cases = []
    for each in array[1:]:
        cases.append((each.split()[0],each.split()[1]))
    cases.sort(key=lambda tup: int(tup[1]))
    cases_dict = {}
    for each in cases:
        cases_dict[each[0]] = each[1]

    results_dict = {}
    for key, value in cases_dict.items():
        peep_dict = {}
        res, peep_dict = stall_calculator_fastest(int(key), int(value))
        results_dict[key] = peep_dict

    for k in range(1,len(array)):
        first, second = results_dict[array[k].split()[0]][int(array[k].split()[1])-1]
        print('Case #' + str(k) + ':', first, second)

def main():
    lines = read_in()
if __name__ == '__main__':
    main()