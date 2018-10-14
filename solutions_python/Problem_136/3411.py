__author__ = 'Gibi'

def time_with_farm(farm, produce, target, max_farm):
    rate = 2.0
    time = 0.0
    for f in range(0, max_farm):
        next_farm_time = farm / rate
        time += next_farm_time
        rate += produce
    time_to_target = target / rate
    return time + time_to_target


f = open("small.txt")
num_tc = int(f.readline().strip())
for tc in range (1, num_tc + 1):
    input = f.readline().strip().split()
    farm = float(input[0])
    produce = float(input[1])
    target = float(input[2])
    max_farm = 0
    best_time = time_with_farm(farm, produce, target, max_farm)
    #print "%d farm best_time %f" % (max_farm, best_time)
    max_farm = 1
    current_time = time_with_farm(farm, produce, target, max_farm)
    #print "%d farm best_time %f" % (max_farm, current_time)
    while current_time < best_time:
        best_time = current_time
        max_farm += 1
        current_time = time_with_farm(farm, produce, target, max_farm)
        #print "%d farm best_time %f" % (max_farm, current_time)
    print ("Case #%d: " % tc) + "{0:.7f}".format(best_time)
    #print ""


