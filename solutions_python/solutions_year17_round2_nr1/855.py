__author__ = 'User'


def get_cruise_speed(track_size, horses):
    slowest = max(finish_time(track_size, start_location, speed) for start_location, speed in horses)
    return track_size / float(slowest)

def finish_time(track_size, start_location, speed):
    return (track_size - start_location) / float(speed)

with open("input.txt", "r") as file:
    with open("result.txt", "w") as write_file:
        num_horses = 0
        problem = 1
        for i, line in enumerate(file):
            if i == 0:
                continue
            if not num_horses:
                horses = []
                track_size, num_horses = line.strip().split()
                track_size, num_horses = int(track_size), int(num_horses)
            else:
                start_location, speed = line.strip().split()
                start_location, speed = int(start_location), int(speed)
                horses.append((start_location, speed))
                num_horses -= 1
                if num_horses == 0:
                    write_file.write("Case #{}: {}\n".format(problem, get_cruise_speed(track_size, horses)))
                    matrix = []
                    problem += 1
