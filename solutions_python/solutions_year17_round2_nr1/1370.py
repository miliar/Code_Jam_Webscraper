# horses is an array of tuples:
# (pos, speed) of horse
#
# output Annie's average speed
def maxSpeed(horses, totalDist):
    # for n horses, find the times of all horses,
    # then get the slowest time and divide totalDist by that time
    largestTime = -1

    for horse in horses:
        start, speed = horse
        time = (totalDist-start)*1.0/speed

        largestTime = max(time, largestTime)

    return totalDist*1.0/largestTime




    # if len(horses) == 1:
    #     start, speed = horses[0]
    #     time = (totalDist - start) * 1.0 / speed
    #     # print totalDist*1.0/time
    #     return totalDist*1.0/time
    # if len(horses) == 2:
    #     start0, speed0 = horses[0]
    #     time0 = (totalDist - start0) * 1.0 / speed0
    #     # print start0, speed0, time0

    #     start1, speed1 = horses[1]
    #     time1 = (totalDist - start1) * 1.0 / speed1
    #     # print start1, speed1, time1


    #     if speed0 > speed1:
    #         if time0 < time1:
    #             # print totalDist*1.0/time1
    #             return totalDist*1.0/time1
    #         else:
    #             return totalDist*1.0/time0
    #     else:
    #         if time0 > time1:
    #             # print totalDist*1.0/time0
    #             return totalDist*1.0/time0
    #         else:
    #             return totalDist*1.0/time1



# def tests():
#     assert(maxSpeed([(2400,5)], 2525) == 101.0)
#     assert(maxSpeed([(120, 60), (60, 90)], 300) == 100.0)
#     assert(maxSpeed([(80,100),(70,10)], 100) == 100.0/3)

# tests()
def main():
    numProblems = int(raw_input())
    num = 1
    while numProblems > 0:
        totalDist, numHorses = raw_input().split(" ")
        totalDist = int(totalDist)
        numHorses = int(numHorses)
        horses = []
        while numHorses > 0:
            start, speed = raw_input().split(" ")
            start = int(start)
            speed = int(speed)
            horses.append((start, speed))
            numHorses -= 1
        print "Case #{}: {}".format(num, maxSpeed(horses, totalDist))

        numProblems -= 1
        num += 1

if __name__ == "__main__":
    main()
