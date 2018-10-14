
#!/usr/bin/env python3

"""
Steed 2: Cruise Control exercise for Code Jam - 2017

Author: Mattia Locatelli
e-mail: mattia.bolob@gmail.com

Developed with Python 3.6.1
"""

def main():

    """
    Main program entry
    """

    num_t = int(input())  # read a line with a single integer

    for i in range(1, num_t + 1):
        tmp = input().split(" ")
        distance, horse_number = int(tmp[0]), int(tmp[1])

        horse_specs = []
        horse_timings = []
        slower_horse_time = 0

        for j in range(0, horse_number):
            
            i_th_horse = input().split(" ")
            i_th_horse_start_position = int(i_th_horse[0])
            i_th_horse_speed = int(i_th_horse[1])
            i_th_horse_time = (distance - i_th_horse_start_position) / i_th_horse_speed

            if i_th_horse_time > slower_horse_time:
                slower_horse_time = i_th_horse_time
            
        annies_horse_speed = distance / slower_horse_time
        print("Case #{}: {:.6f}".format(i, annies_horse_speed))

if __name__ == '__main__':
    main()
