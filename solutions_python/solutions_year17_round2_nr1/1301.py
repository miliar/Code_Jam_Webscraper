import sys  

def calc_horses(miles, horses_list):
    max_horse_time = 0.0
    for horse in horses_list:
        start_mile = horse[0]
        speed = horse[1]
        time = float(miles - start_mile) / float(speed)
        if time > max_horse_time:
            max_horse_time = time
    
    return miles / max_horse_time
        
def main():
    input = open(sys.argv[1], 'rb').readlines()
    number_of_cases = int(input.pop(0))
    horses_list = []
    i=0
    while len(input) != 0:
        miles, horses = input.pop(0).split(" ")
        miles = int(miles)
        horses = int(horses)
        for horse in range(horses):
            start_mile, max_speed = input.pop(0).split(" ")
            horses_list.append((int(start_mile), int(max_speed)))
        
        ans = calc_horses(miles, horses_list)
        print "Case #%d: %.6f" % (i+1, ans)
        i=i+1
        horses_list = []
        
if __name__ == "__main__":
    main()


    