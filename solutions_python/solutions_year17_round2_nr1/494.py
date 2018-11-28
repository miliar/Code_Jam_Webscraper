#!/usr/bin/python
with open("A-large.in") as f:
    testCases = []
    lines = f.read().split("\n")
    caseNum = int(lines[0])
    i = 1
    for j in range(caseNum):
        dest, horseNum = float(lines[i].split(" ")[0]), int(lines[i].split(" ")[1])
        testCases.append({"dest": dest, "horses": []})
        i += 1
        for k in range(horseNum):
            pos, speed = float(lines[i].split(" ")[0]), float(lines[i].split(" ")[1])
            i += 1
            testCases[-1]["horses"].append({"pos": pos, "speed": speed, "diff": testCases[-1]["dest"] - pos})
            testCases[-1]["horses"][-1]["time"] = testCases[-1]["horses"][-1]["diff"] / testCases[-1]["horses"][-1]["speed"]
    i = 1
    for case in testCases:
        horses = case["horses"]
        horses.sort(key=lambda c: c["time"], reverse = True)
        minTime = horses[0]['time']
        dest = case['dest']
        speed = dest / minTime
        print("Case #%d: %f" % (i, speed))
        i += 1
