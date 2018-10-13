import sys


def get_max_speed(distance, horses, current_time):
    # print "num horses considered: " + str(len(horses))
    if len(horses) == 1:
        time_taken = (distance - horses[0][0]) / (horses[0][1] + 0.0)
        return distance / (time_taken + current_time)
    horses.sort(key=lambda tup: tup[0])
    # print horses
    horse1 = horses.pop(0)
    horse2 = horses.pop(0)
    if horse1[1] == horse2[1]:
        # same rate, we only care about the one further behind
        new_horse = (min(horse1[0], horse2[0]), horse1[1])
        horse_to_insert = new_horse
        addtional_time = 0
    else:
        meeting_time = (horse2[0] - horse1[0]) / (horse1[1] - horse2[1] + 0.0)
        meeting_distance = horse1[0] + meeting_time * horse1[1]
        # print "Meeting distance: " + str(meeting_distance) + ", time: " + str(meeting_time)
        if meeting_time < 0 or meeting_distance > distance:
            # insert the further behind horse: it will never catch up
            horse_to_insert = horse1
            addtional_time = 0
        else:
            # new horse at intersection point, with slower rate (we know horse2 is slower)
            horse_to_insert = (meeting_distance, horse2[1])
            addtional_time = meeting_time
    horses.insert(0, horse_to_insert)
    return get_max_speed(distance, horses, current_time + addtional_time)

def main(filename):
    # print "Reading from: ", filename
    with open(filename) as f:
        num_entries = int(f.readline())
        for i in range(num_entries):
            distance, nun_horses = map(int, f.readline().split())
            horses = []
            for j in xrange(nun_horses):
                horses.append(map(int, f.readline().split()))
            solution = get_max_speed(distance, horses, 0)
            print "Case #" + str((i + 1)) + ": " + str(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "You should provide the input file name"
    else:
        main(sys.argv[1])