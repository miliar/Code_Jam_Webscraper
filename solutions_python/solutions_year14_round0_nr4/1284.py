import sys
import bisect
def analyze(naomi, ken, N):
    naomi_sorted = sorted(naomi)
    ken_sorted = sorted(ken)
    left_idx = 0
    ken_wins_normal = 0
    naomi_cheat = 0
    # normal play
    for i in naomi_sorted:
        #find place of insertion in ken_sorted
        insert_idx = bisect.bisect_right(ken_sorted, i, left_idx)
        #insert index represents the p
        if insert_idx < N:
            ken_wins_normal +=1
        else:
            break
        left_idx = insert_idx+1
    naomi_normal = N - ken_wins_normal

    #deceitful
    #strategy is to force ken to play his maxes on naomis mins
    #for every one we have to conceed, make him pay a high fee for it
    track_ken = 0
    for i in naomi_sorted:
        if i > ken_sorted[track_ken]:
            naomi_cheat += 1
            track_ken +=1
        else: #we just assume that ken played his biggest
            pass
    return (naomi_cheat, naomi_normal)

if __name__ == "__main__":
    output_file = open("%s.%s"%(sys.argv[1].split(".")[0],"out"),"w")
    file_name = sys.argv[1]
    input_file = open(file_name)
    case_count = int(input_file.readline())
    for i in xrange(case_count):
        #block count
        N = int(input_file.readline().strip())
        naomi = map(float, input_file.readline().strip().split(" "))
        ken = map(float, input_file.readline().strip().split(" "))
        result = analyze(naomi, ken, N)
        output_file.write("Case #%s: %s\n"%(i+1, " ".join(map(str,result))))
    output_file.close()
    input_file.close()
    print "Done!"

#TODO: precompute len, saves O(n) :D