from os import path, linesep
import itertools
import math

class Room:
    pass

def solve_case(cj_input):
    """
    Solves one case of this CodeJam task and returns its solution.
    Read a line by calling 
       next(cj_input)
    """
    # get room specs and room
    room_specs = list(map(int, next(cj_input).split(" ")))
    height = room_specs[0]
    width = room_specs[1]
    vision = room_specs[2]
    print(height, width, vision)
    
    # contruct room 
    room = get_room(height, width, cj_input)
    
    # find out how many mirrors
    return calculate_images(room, vision) 


def get_room(height, width, cj_input):
    """
    Reads in room information.
    """
    # GET A ROOM :D
    room = Room()
    room.inner_width = width - 2
    room.inner_height = height - 2
    room.data = []
    
    # skip first and last row, only read inner room
    next(cj_input)
    for i in range(1, height-1):
        room.data.append(next(cj_input)[1:-1])
    next(cj_input)
    
    # find own position and mirrors
    room.mirrors = []
    room.position = (0, 0)
    for y in range(room.inner_height):
        for x in range(room.inner_width):
            here = room.data[y][x]
            if here == "#":
                room.mirrors.append((x,y))
            elif here == "X":
                room.position = (x,y)
    
    return room


def calculate_images(room, vision):
    """
    Calculates how many images we can see.
    """
    room.position = room.position[0] + 0.5, room.position[1] + 0.5 
    visible_images = 0
    used_directions_left = set()
    used_directions_right = set()
    for n in range(1, vision+1):
        for delta_y in range(-n,n+1,1):
            for delta_x in range(-n,n+1,1):
                # no 0-0 check
                if delta_x == delta_y == 0:
                    continue
                
                # get mirrored coords
                mirrored_coords = calc_mirror_coords(room, delta_x, delta_y)
                #print(delta_x, delta_y, mirrored_coords)
                
                # check if we can still see it
                distance = math.sqrt((mirrored_coords[0]-room.position[0])**2 + (mirrored_coords[1] - room.position[1])**2)
                if distance <= vision:
                    # calculate direction
                    direction = 0
                    if room.position[0] == mirrored_coords[0]:
                        if room.position[1] < mirrored_coords[1]:
                            direction = "straight down"
                        else: direction = "straight up"
                    elif room.position[1] == mirrored_coords[1]:
                        direction = "even line"
                    else:
                        direction = (room.position[1] - mirrored_coords[1]) / (room.position[0] - mirrored_coords[0])
                    
                    # goes left or right?
                    correct_directions_set = used_directions_right
                    if mirrored_coords[0] < room.position[0]:
                        correct_directions_set = used_directions_left
                    
                    if direction in correct_directions_set:
                        continue
                    correct_directions_set.add(direction)
                    visible_images += 1
                
    
    return str(visible_images)

def calc_mirror_coords(room, delta_x, delta_y):
    """
    Calculates mirrored coordinates of own position (delta_x rooms in x position, delta_y rooms in y position).
    """
    result_x = 0
    result_y = 0
    if delta_x % 2 == 1:
        result_x = -room.position[0] + (delta_x + 1) * room.inner_width
    else:
        result_x = room.position[0] + delta_x * room.inner_width
    if (delta_y % 2 == 1):
        result_y = -room.position[1] + (delta_y + 1) * room.inner_height
    else:
        result_y = room.position[1] + delta_y * room.inner_height

    return (result_x, result_y)


# From here on, the fairly generic CodeJam code follows. Read in file, output solutions.
# Potentially the first line does not include number of cases, this may have to be adapted.

def run_codejam():
    """
    Runs the codejam by initializing input and output, calling methods which solve the cases and finally
    outputting the results.
    """
    testfile = "D-small-attempt0"
    cases_file = path.join(path.dirname(__file__), testfile)
    with open(cases_file + ".in", "r") as cj_input:
        with open(cases_file + ".out", "w") as cj_output:
            # get a line-based reader
            reader = iter(cj_input.read().splitlines())
            
            # read number of cases
            caseCount = int(next(reader))
            
            # handle cases (1-based)
            for i in range(1, caseCount+1):
                result = solve_case(reader)
                outputStr = "Case #" + str(i) + ": " + result
                cj_output.write(outputStr + "\n")
                print(outputStr)
        
# run the CodeJam analysis
run_codejam()