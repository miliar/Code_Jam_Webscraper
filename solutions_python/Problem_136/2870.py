def time_to_win(cps, goal):
    return goal/cps

def factory_time(cps, factorycost):
    return factorycost/cps

def clicker(cps, factorycost, factoryproduction, goal):
    if time_to_win(cps, goal) < factory_time(cps, factorycost) + time_to_win(cps+factoryproduction, goal):
        return time_to_win(cps, goal)
    time = 0.0
    while time_to_win(cps, goal) > factory_time(cps, factorycost) + time_to_win(cps+factoryproduction, goal):
        time += factory_time(cps, factorycost)
        cps = cps+factoryproduction
    return time + time_to_win(cps, goal)

def main():
    cases = input()
    for i in range(1, cases+1):
        inputs = [float(x) for x in raw_input().split(" ")]
        factorycost = inputs[0]
        factoryproduction = inputs[1]
        goal = inputs[2]
        cps = 2.0
    
        print("Case #" + str(i) + ": %.7f" % clicker(cps, factorycost, factoryproduction, goal))
    return None

if __name__=="__main__":
    main()
