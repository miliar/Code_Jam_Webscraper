import sys
import copy
colors = ['R','O','Y','G','B','V']

def get_ints(line):
    start = 0
    to_return = []
    while start < len(line):
        end = line.find(' ', start)
        if end == -1:
            end = len(line)
        to_return.append(int(line[start:end]))
        start = end+1
    return to_return

#first element is NOT the number of horses
def get_most_two_horses(horses):
    biggest = 0
    size = horses[0]
    for i in range(1,len(horses)):
        if horses[i] > size:
            biggest = i
            size = horses[i]
    second = 0
    size = horses[0]
    if biggest == 0:
        second = 1
        size = horses[1]
    for i in range(1,len(horses)):
        if horses[i] > size and i != biggest:
            second = i
            size = horses[i]
    return [colors[biggest], colors[second]]

#assume there is at least one horse left
#assumes first index is NOT number of horses
#removes whatever horse is placed from horses
def place_next_horse(circle, horses):
    #print circle
    #print horses
    last_horse = circle[len(circle)-1]
    first = get_most_two_horses(horses)[0]
    second = get_most_two_horses(horses)[1]
    #print first+'  '+second
    #print colors.index(first)
    first_i = colors.index(first)
    second_i = colors.index(second)
    #print str(first_i)+'  '+str(second_i)
    assert horses[first_i] > 0
    assert horses[second_i] >= 0
    num_second = horses[second_i]
    
    if first != last_horse:
        horses[first_i] -= 1
        return circle+first
    if num_second <= 0:
        print horses
        assert False
    horses[second_i] -= 1
    return circle+second
    
def place_first_horse(horses):
    first = get_most_two_horses(horses)[0]
    first_i = colors.index(first)
    horses[first_i] -= 1
    return first

def num_horses(horses):
    total = 0
    for num in horses:
        total+=num
    return total

def make_circle(horses):
    horses.pop(0)
    circle = place_first_horse(horses)
    while num_horses(horses) > 0:
        circle = place_next_horse(circle,horses)
    return circle

    
def is_possible(horses):
    num_horses = horses[0]
    largest = int(num_horses/2)
    for i in range(1,len(horses)):
        if horses[i] > largest:
            return False
    return True

def swap_last_horses(circle):
    last = circle[len(circle)-1]
    second = circle[len(circle)-2]
    first = circle[0]
    if first == last:
        to_return = circle[:len(circle)-2]+last+second
        return to_return
    else:
        return circle
    
def solution(horses):
    cont = is_possible(horses)
    if not cont:
        return 'IMPOSSIBLE'
    circle = make_circle(horses)
    circle = swap_last_horses(circle)
    return circle
    

def check_solution(sol, horses):
    if sol == 'IMPOSSIBLE':
        return True
    horses.pop(0)
    if sol[0] == sol[len(sol)-1]:
        print 'end matches front'
        return False
    counts = [0,0,0,0,0,0]
    last_horse = sol[0]
    counts[colors.index(last_horse)]+=1
    for i in range(1,len(sol)):
        if sol[i] == last_horse:
            print "index %d does matches last"%i
            return False
        last_horse = sol[i]
        counts[colors.index(last_horse)]+=1
    if counts != horses:
        print 'error in counts'
        return False
    return True

in_file = sys.argv[1]
in_stream = open(in_file)
lines = in_stream.readlines()
i = 1
case_num = 1
while i < len(lines):
    horses = get_ints(lines[i])
    check = copy.deepcopy(get_ints(lines[i]))
    sol = solution(horses)
    #print lines[i]
    assert check_solution(sol,check), case_num
    #print "Case %d: "%case_num +str(lines[i])
    #print horses
    print "Case #%d: "%case_num + sol
    i += 1
    case_num += 1
    
        
