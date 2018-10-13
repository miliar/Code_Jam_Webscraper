read_file = open('D-small-attempt0.in','r')

n_cases = int(read_file.readline())

#n_cases = int(raw_input())

for i in range(n_cases):
    #L = raw_input().split(" ")
    L = read_file.readline().split(" ")

    X = int(L[0])
    R = int(L[1])
    C = int(L[2])

    if R*C % X != 0:
        print("Case #"+str(i+1)+": RICHARD")
        continue
    if X % 2 == 1 and X >= 3:
        if R < (X+1)/2 or C < (X+1)/2:
            print("Case #"+str(i+1)+": RICHARD")
            continue
    if X % 2 == 0 and X >= 4:
        if R < X/2 + 1 or C < X/2 +1:
            print("Case #"+str(i+1)+": RICHARD")
            continue
    if X >= 7:
        print("Case #"+str(i+1)+": RICHARD")
        continue
   
    print("Case #"+str(i+1)+": GABRIEL")
