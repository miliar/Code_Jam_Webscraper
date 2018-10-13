import sys

def main():
    files = ["B-practice.in","B-large.in","A-large-practice.in"]
    content = file(files[1])
    cases = int(content.readline())

    filename = "output.txt"
    File = open(filename,'w')

    for i in range(cases):
        case = content.readline().split()
    
        for j in range(len(case)):
            case[j] = int(case[j])

        numGooglers = int(case[0])
        surpriseScores = int(case[1])
        threshold = int(case[2])
        scores = case[3:]
    
        
        if(surpriseScores < 1):
            solution = noSurprise(scores, threshold)
            File.write("Case #%d: %s" % (i+1, solution) + "\n")
            
        else:
            solution = surprise(scores, threshold, surpriseScores)
            File.write("Case #%d: %s" % (i+1, solution) + "\n")

def surprise(scores, threshold, surpriseScores):
    #print 'Surprise',scores , "Threshold",threshold
    solution = 0
    surprisesFound = 0
    for num in scores:
        breakdown = []
        avg = num//3
        if(num%3 == 0 and num//3 >= threshold):
            breakdown = [num//3] * 3
            solution = solution +1
            #print breakdown , "solution" , solution
        else:
            breakdown = [threshold, num//3 , num//3]
            while( sum(breakdown) != num):
                if(sum(breakdown) < num):
                    minval = min(breakdown)
                    minval = minval + 1
                    breakdown.remove(min(breakdown))
                    breakdown.append(minval)
                if(sum(breakdown) > num):
                    minval = min(breakdown[1:])
                    minval = minval - 1
                    breakdown.remove(min(breakdown[1:]))
                    breakdown.append(minval)
            if [x for x in breakdown if x < 0 or x <(threshold-2)]:
                pass
                #print breakdown, " Not a solution"
            elif [x for x in breakdown if x <(threshold-1)]:
                if(surprisesFound >= surpriseScores):
                    pass
                    #print breakdown,'cannot count this surprise solution'
                else:
                    solution = solution +1
                    surprisesFound = surprisesFound + 1
                    #print breakdown, 'surprise!', "solution", solution       
            else:
                solution = solution + 1
                #print breakdown ,'normal solution', solution
    return solution
                
        


def noSurprise(scores, threshold):
    #print 'no surprise' , scores , "Threshold",threshold
    solution = 0
    for num in scores:
            breakdown = []
            avg = num//3
            if(num%3 == 0 and num//3 >= threshold):
                breakdown = [num//3] * 3
                solution = solution + 1
                #print breakdown , "solution" , solution
            else:
                breakdown = [threshold, num//3 , num//3]
                while( sum(breakdown) != num):
                    if(sum(breakdown) < num):
                        minval = min(breakdown)
                        minval = minval + 1
                        breakdown.remove(min(breakdown))
                        breakdown.append(minval)
                    if(sum(breakdown) > num):
                        minval = min(breakdown[1:])
                        minval = minval - 1
                        breakdown.remove(min(breakdown[1:]))
                        breakdown.append(minval)
                if [x for x in breakdown if x < (threshold-1)]:
                    #print breakdown , " Not a solution"
                    pass
                else:
                    solution = solution + 1
                    #print breakdown , "solution" , solution
    return solution
            
    
main()
                


