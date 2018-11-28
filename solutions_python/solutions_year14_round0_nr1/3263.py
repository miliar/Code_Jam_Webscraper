def main():
    f = open("input.txt", "r")
    entries = f.readline().strip()
    for count in xrange(1, int(entries) + 1):
        set1 = []
        set2 = []
        answer1 = int(f.readline().strip())
        for row in xrange(1, 5):
            set1.append(f.readline().strip().split(" "))
            #print row;
        answer2 = int(f.readline().strip())
        for row in xrange(1, 5):
            set2.append(f.readline().strip().split(" "))
            #print row;
        res = list(set(set1[answer1-1]) & set(set2[answer2-1]))
        answer = ""
        if len(res) == 0:
            answer = "Volunteer cheated!"
        elif len(res) > 1:
            answer = "Bad Magician!"
        else:
            #print res;
            answer = res[0]
        
        #print count
        print "Case #{}: {}".format(count, answer)
    #print entries
    f.close()
    
    
    
def readline():
    pass

if __name__ == "__main__":
    main()