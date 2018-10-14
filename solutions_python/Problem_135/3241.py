text_file = "C:\Users\Public\googlejamq.txt"

def main():
    f = open(text_file, 'r')
    tricks = f.readline()
    cards = ""
    for trick in range(0,int(tricks)):
        first_set = getSet(f)
        second_set = getSet(f)
        result = compareSets(first_set, second_set)
        if len(result) is 1:
            print "Case #%i: %s" % (trick+1, result[0])
        elif len(result) is 0:
            print "Case #%i: Volunteer cheated!" % int(trick+1)
        else:
            print "Case #%i: Bad magician!" % int(trick+1)

def compareSets(a,b):
    return [i for i in a if i in b]
    
def getSet(f):
    answer =  f.readline()
    for row in range(0,4):
            if row is (int(answer) -1):
                result = f.readline()
            else:
                f.readline()
    result = result.split()
    return result
    
if __name__ == "__main__":
    main()
    
