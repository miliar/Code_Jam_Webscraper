#/usr/bin/env python

import sys

DEBUG = False
def debug(string):
    if DEBUG:
        print string

def other(robot):
    if robot == "O":
        return "B"
    elif robot == "B":
        return "O"
    else:
        raise Error

def find_next_target(movs, info, robot):
    idx = info[robot]["next_idx"]
    if idx == len(movs) - 2:
        info[robot]["next"] = -1
        info[robot]["next_idx"] = -1
        return False
    for i in range(idx+2, len(movs), 2):
        if movs[i] == robot:
            info[robot]["next"] = movs[i + 1]
            info[robot]["next_idx"] = i
            return True
    info[robot]["next"] = -1
    info[robot]["next_idx"] = -1
    return False

def next_action(movs, info, robot):
    if info[robot]["next"] == -1:
        msg = "Finished"
    else:
        if str(info[robot]["cur"]) == str(info[robot]["next"]):
            if info["gen"]["current_idx"] == info[robot]["next_idx"]:
                info["gen"]["next_idx"] = info["gen"]["current_idx"] + 2
                info["gen"]["current_idx"] = -10
                msg = "Push " + str(info[robot]["cur"])
                find_next_target(movs, info, robot)
            else:
                msg = "Stay at " + str(info[robot]["cur"])
        else:
            msg = "Move from %s to %s" % (str(info[robot]["cur"]), str(info[robot]["next"]))
            if int(info[robot]["next"]) > int(info[robot]["cur"]):
                info[robot]["cur"] += 1
            else:
                info[robot]["cur"] -= 1
    return msg
    
def print_status(seconds, action_o, action_r):
    return "%s | %s | %s" % (seconds, action_o, action_r)


in_file = sys.argv[1]
fp = open(in_file)
for case in range (1, int(fp.readline())+1):
    debug("Case %s: " % (case))
    seconds = 0
    movs = fp.readline().split()
    debug(movs)
    debug("T | Orange       | Blue")
    movs_number = int(movs[0])
    info = {
        "gen": {
            "current_idx": 1,
            "next_idx": -1
        },
        "O": {
            "cur": 1,
            "next": -1,
            "next_idx": -1
        },
        "B": {
            "cur": 1,
            "next": -1,
            "next_idx": -1
        }
    }
    find_next_target(movs, info, "O")
    find_next_target(movs, info, "B")
    while(True):
        seconds +=1
        action_o = next_action(movs, info, "O")
        action_r = next_action(movs, info, "B")
        if info["gen"]["current_idx"] == -10:
            info["gen"]["current_idx"] = info["gen"]["next_idx"]
            info["gen"]["next_idx"] = -10
        debug(print_status(seconds, action_o, action_r))
        if info["O"]["next_idx"] == -1 and info["B"]["next_idx"] == -1:
            break
        # For testing purposes
        #if seconds == 10:
        #    break
    print "Case #%s: %s" % (str(case), seconds)
    # For testing purposes
    #if case == 1:
    #    break
    debug("")