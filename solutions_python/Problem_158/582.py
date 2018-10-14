# Only for small input. Will not work for large.
for n in range(int(input())):
    X, R, C = map(int, input().split())
    # reverse engineered the entire thing.
    # did this shit with pen+paper with a bunch or trial and error sample problems
    # there has to be a better way (one that I don't know of)
    # DO NOT DO THIS FOR LARGE DATASET. THIS WORKS ONLY FOR SMALL
    # @Google people - if you are reading this hire me :)
    re = True
    #will be false since board size for small is 4 (no way it will fit)
    if (X>= 7):
        re = False
    elif ((X >R) and (X > C)):
        re =False
    elif ((R * C % X) != 0):
        re = False
    elif (((X + 1) // 2) > min(R, C)):
        re= False
    elif X in (1, 2, 3):
        re= True
    elif (X == 4):
        re = min(R, C) > 2
    elif (X == 5):
        re = not(min(R, C) == 3 and max(R, C) == 5)
    elif (X == 6):
        re = min(R, C) > 3
    print('Case #%d:' % (n + 1), 'GABRIEL' if re else 'RICHARD')
