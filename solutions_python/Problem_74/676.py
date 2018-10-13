import copy

def function2(fi,fo):
    f = open(fi)
    f2 = open(fo,"w")
    cases = int(f.readline())
    for nc,case in enumerate(range(cases)):
        test = f.readline()[0:-1].split(" ")
        # ----------------------------------
        # Code here
        # ---------------------------------
        nb = int(test[0])
        robotPos = 1
        botonPos = 2
        cont = 0
        position = {"O":1,"B":1}
        eventStack = []
        events = test[1:]
        time = 0
        while events != []:
            firstO = ("O","end",float("inf"),float("inf"))
            for ne,e in enumerate(events):
                if events[ne] == "O":
                    firstO = ("O",int(events[ne+1]),abs(int(events[ne+1])-position["O"]),ne)
                    break
            firstB = ("B","end",float("inf"),float("inf"))
            for ne,e in enumerate(events):
                if events[ne] == "B":
                    firstB = ("B",int(events[ne+1]),abs(int(events[ne+1])-position["B"]),ne)
                    break
            nextEvents = [firstO,firstB]
            nextEvents.sort(key=lambda x: x[3])
            nextEvent = nextEvents[0]
            eventStack += [nextEvent,(nextEvent[0],"P",1,-1)]
            events.pop(nextEvent[3])
            events.pop(nextEvent[3])
            position[nextEvent[0]] = nextEvent[1]
            otherEvent = nextEvents[1]
            if otherEvent[2] <= nextEvent[2]:
                position[otherEvent[0]] = otherEvent[1]
            else:
                if otherEvent[1] > position[otherEvent[0]]:
                    position[otherEvent[0]] += nextEvent[2] + 1
                else:
                    position[otherEvent[0]] -= (nextEvent[2] + 1)
        time = 0
        print "------------------" + "Case #" + str(nc+1)
        for i in eventStack:
            time += i[2]
        serie = ""
        for i in range(0,len(eventStack),2):
            serie += str(eventStack[i][0]) + str(eventStack[i][1]) + " "
        print serie
        print eventStack
        print time
        text = "Case #" + str(nc+1) + ": "  + str(time)
        f2.write(text + "\n")
        
#function2("robots.in","test.txt")
#function2("short.in","short.txt")
function2("long.in","long.txt")

