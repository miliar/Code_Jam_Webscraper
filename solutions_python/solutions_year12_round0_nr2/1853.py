def generate_combinations():

    combinations = dict([(i,[]) for i in range(0,31)])

    #Somewhat sloppy, but if it works it works.
    #LOLOLOL
    for score1 in range(11):
        for score2 in range(11):
            for score3 in range(11):
                max_diff = max(abs(score1-score2),abs(score3-score2),abs(score3-score1))
                if max_diff <=2:
                    total = score1+score2+score3
                    triplet = [score1,score2,score3]
                    triplet.sort()
                    triplet = (triplet,False if max_diff<2 else True)
                    if triplet not in combinations[total]:
                        combinations[total].append(triplet)
    return combinations


def solve(total_scores,num_surprising, p, combinations, at_least_p,tabs,verbose=False):

    max_score = None
    possibilities = combinations[total_scores[0]]
    possibilities = filter(lambda i: not i[1], possibilities) if num_surprising==0 else possibilities
    if len(total_scores)==1:
        for possibility in possibilities:
            num_surprising2 = num_surprising-1 if possibility[1] else num_surprising
            

            max_score = max(possibility[0])
            if num_surprising2==0:
                at_least_p2= at_least_p+1 if max_score>=p else at_least_p
                if verbose: print tabs,possibility,"--",at_least_p2
                return at_least_p2
            else:
                return None

    else:
        max_over_p = None
        for possibility in possibilities:
            num_surprising2 = num_surprising-1 if possibility[1] else num_surprising
            
            max_score = max(possibility[0])
            at_least_p2 = at_least_p+1 if max_score>=p else at_least_p
            if verbose: print tabs,possibility,"--",at_least_p2
            result = solve(total_scores[1:],num_surprising2,p,combinations,at_least_p2,tabs+"\t")
            if result > max_over_p: max_over_p = result
        return max_over_p
                
                
c = generate_combinations()
lines = open("q2.txt").readlines()
num_tests = int(lines[0])
tests = lines[1:]
for i in range(len(tests)):
    test = tests[i]
    test = [int(x) for x in test.split(" ")]
    n = test[0]
    s = test[1]
    p = test[2]
    scores=test[3:]
    print "Case #"+str(i+1)+":",solve(scores,s,p,c,0,"")

