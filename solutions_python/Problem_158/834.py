import jamFileProcessor as jfp
myjfp = jfp.JamFileProcessor("D-small-attempt8", 1)

case = myjfp.readcase()
while case:
    case = case[0]
    x = int(case[0])
    r = int(case[1])
    c = int(case[2])
    if ((x < 4 and r >= x/2 and c >= x/2) or (x >= 4 and r >= x//2 + 1 and c >= x//2 + 1)) and (r >= x or c >= x) and r*c % x == 0:
        myjfp.writecase("GABRIEL")
    else:
        myjfp.writecase("RICHARD")
    case = myjfp.readcase()
