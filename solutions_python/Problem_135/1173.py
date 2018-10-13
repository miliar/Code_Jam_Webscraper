def get_arrangement():
    result = []
    for i in range(4):
        result.append(map(int, raw_input("").split(" ")))
    return result

if __name__ == "__main__":
    T = int(raw_input(""))
    for t in xrange(1, T+1):
        answer1 = int(raw_input(""))
        arrange1 = get_arrangement()
        answer2 = int(raw_input(""))
        arrange2 =get_arrangement()
        set1 = set(arrange1[answer1-1])
        set2 = set(arrange2[answer2-1])
        magicTrick = set1 & set2
        if len(magicTrick) == 0:
            result = "Volunteer cheated!"
        elif len(magicTrick) > 1:
            result = "Bad magician!"
        else:
            result = str(list(magicTrick)[0])
        print "Case #%d: %s" % (t, result)