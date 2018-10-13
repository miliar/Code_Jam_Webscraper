#!/usr/bin/python
#Bot Trust - Andrey Polyakov
import re

class data():
    seconds = 0
    wait_on = "sfd"
    o_loc = 1
    b_loc = 1
    o_target = -1
    b_target = -1
    cases = -1
    curr_case = 1
    lines = []
    full_list = [] 

def init(data):
    try:
        f = open("file.in", "r")
    except IOError:
        print "File not found!"
        exit()
    data.lines = f.readlines()
    f.close()
    data.cases = int(data.lines[0])
    
def init_case(data):
    data.full_list = re.findall("[O|B].[0-9]*", data.lines[data.curr_case])

def target(data):
    if(len(data.full_list) == 0):
        return    
    if(data.full_list[0][0] == 'O'):
        data.wait_on = "ORANGE"
        data.o_target = int(data.full_list[0][2:])
        data.b_target = -1        
        for x in range(len(data.full_list)):
            if data.full_list[x][0] == 'B':
                data.b_target = int(data.full_list[x][2:])
                break
    else:
        data.wait_on = "BLUE"
        data.b_target = int(data.full_list[0][2:])
        data.o_target = -1
        for x in range(len(data.full_list)):
            if data.full_list[x][0] == 'O':
                data.o_target = int(data.full_list[x][2:])
                break    

def main():
    init(data)
    for w in range(data.cases):
        init_case(data)
        target(data)
        while len(data.full_list) != 0:  
            if data.wait_on == "ORANGE":
                if data.o_target == data.o_loc:
                    del(data.full_list[0])
                    move_blue(data)
                    target(data)
                else:
                    move_orange(data)
                    move_blue(data)
            else:
                if data.b_target == data.b_loc:
                    del(data.full_list[0])
                    move_orange(data)
                    target(data)
                else:
                    move_orange(data)
                    move_blue(data)            
            data.seconds += 1
        print "Case #" + str(data.curr_case) + ": " + str(data.seconds)
        data.curr_case += 1
        data.seconds = 0
        data.wait_on = "sfd"
        data.o_loc = 1
        data.b_loc = 1
        data.o_target = -1
        data.b_target = -1

def move_orange(data):
    if data.o_loc - data.o_target > 0:
        data.o_loc -= 1
    elif data.o_loc - data.o_target < 0:
        data.o_loc += 1
def move_blue(data):
    if data.b_loc - data.b_target > 0:
        data.b_loc -= 1
    elif data.b_loc - data.b_target < 0:
        data.b_loc += 1

if __name__ == "__main__":
    main()
