__author__ = 'RTSwan'

def get_lines(infile):
    """Returns a list containing the lines in a file, supplied as infile"""
    file = open(infile, "r")
    linesTemp, lines = [], []
    for i in file:
        linesTemp.append(i)
    file.close()
    for i in linesTemp:
        lines.append(i.replace("\n", ""))
    return lines


def next_farm_time(cps, cost):
    """Returns the amount of time it would take to purchase a new farm"""
    return cost/cps

def next_win_time(cps, win):
    """Returns the amount of time it would take to get enough cookies to win"""
    return win/cps

def win_after_farm(cps, cost, win, farmprodspeed):
    nextfarm = next_farm_time(cps, cost)
    farmafterwin = next_win_time(cps + farmprodspeed, win) #adds production speed of new farm
    return nextfarm + farmafterwin


def CookieClicker(infile, outfile):
    lines = get_lines(infile)
    outputfile = open(outfile, "w")
    cases = eval(lines[0])
    count = 1  # keep track of index in lines list
    for i in range(cases):
        time = 0
        cps = 2  # cookies per second
        farm_cost, production, win_amount = eval(lines[count].replace(" ", ","))
        count += 1  # move index to next line for next iteration
        while next_win_time(cps, win_amount) > win_after_farm(cps, farm_cost, win_amount, production):
            time += next_farm_time(cps, farm_cost)
            cps += production
        time += next_win_time(cps, win_amount)  # out of loop, therefore shortest route
        print("Case #" + str(i + 1) + ": " + str(time), file=outputfile)
    outputfile.close()

if __name__ == '__main__':
    CookieClicker("B-large.in", "B-large-output.txt")