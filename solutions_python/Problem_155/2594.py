for t in range(int(input())):
    smax, shystring = [i for i in input().split()]
    stoodup = int(shystring[0])
    friendsinserted = 0
    for i in range(1, int(smax)+1):
        if int(shystring[i]):
            if i > stoodup:
                friendsinserted += (i - stoodup)
                stoodup += (i - stoodup)
            stoodup += int(shystring[i])
    print('Case #%d: %d' %(t+1, friendsinserted))