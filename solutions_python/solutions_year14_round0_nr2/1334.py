#!/usr/bin/python

def cookie_clicker_min(c, f, x):
    farms = 0
    time_building_farms = 0
    start_speed = 2
    quickest = x / start_speed
    while time_building_farms < quickest:
        time_building_farms += c / (start_speed + farms * f)
        farms += 1
        current = time_building_farms + x / (start_speed + farms * f)
        if (current - quickest < -1e-8):
            quickest = current
    return format(quickest, '.7f')

def main():
    with open('input.in', 'r') as f:
        with open('output.txt', 'w') as o:
            n = int(f.readline().rstrip('\n'))
            for i in range(n):
                parameters = list(map(float, f.readline().rstrip('\n').split(' ')))
                result = "Case #" + str(i + 1) + ": " + cookie_clicker_min(parameters[0], parameters[1], parameters[2])
                print(result)
                o.write(result + "\n")

if __name__=="__main__":
    main()
