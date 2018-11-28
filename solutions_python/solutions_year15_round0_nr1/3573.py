def ovation():
    for test in range(int(raw_input())):
        case = raw_input().split()
        shy = 0
        people = 0
        needed = 0
        for i in case[1]:
            if people >= shy:
                people += int(i)
            elif int(i) > 0:
                needed += (shy - people)
                people += needed + int(i)
            shy += 1
        print "Case #"+str(test+1)+": " + str(needed)

if __name__ == "__main__":
    ovation()
