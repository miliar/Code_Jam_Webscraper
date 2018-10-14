#! /usr/bin/pypy

def aboveThreshNotSurprising(t,p):
    for a in range(p,11): #till max score, largest(or at least equal to others)
        thresh = max(0,a-1)-1
        for b in range(a,thresh,-1):
            for c in range(b,thresh,-1):
                if a+b+c == t: #found one
                    return True

    return False

def aboveThreshSurprising(t,p):
    for a in range(p,11): #till max score, largest(or at least equal to others)
        s = a*3-4 #the lowest it can get
        if s > t:
            return False

        thresh = max(0,a-2)-1

        for b in range(a,thresh,-1):
            for c in range(b,thresh,-1):
                if a+b+c == t: #found one
                    return True

    return False

# returns if number t has a decomposition which reaches p
# returns: (not surprising,surprising)
def aboveThresh(t,p):
    result = [False,False]

    result[0] = aboveThreshNotSurprising(t,p)
    result[1] = aboveThreshSurprising(t,p)

    return result

def solve(N,S,p,ti): #googlers, #strange, thresh, [score]
    ti = map(lambda x: aboveThresh(x,p), ti)
    bins = [0,0,0,0] # ft |tt ff| tf -> good to be strange, neutral, baed m'kay

    result = 0
    #distribute strange scores in best possible way
    for notStrange,strange in ti:
        if not notStrange and strange: #ft
            bins[0] += 1
        elif notStrange and strange: #tt
            bins[1] += 1
        elif not notStrange and not strange: #ff
            bins[2] += 1
        elif notStrange and not strange: #tf
            bins[3] += 1

    # as S <= N no error handling is needed
    while S > 0:
        if bins[0] > 0: #yeii
            result += 1
            bins[0] -= 1
        elif bins[1] > 0: #okay
            result += 1
            bins[1] -= 1
        elif bins[2] > 0: #still okay
            bins[2] -= 1
        else: # oh no!
            bins[3] -= 1

        S -= 1

    #add not strange which have not been yet used
    result += (bins[1]+bins[3])
                
    return result

def processFile(filename):
    f = open(filename, "r")
    resultFile = open("result.txt","w")

    T = int(f.readline()) #number of cases
    print "Solving %s cases:"%(T,)

    #read the other lines
    solutions = [] 
    for i,line in enumerate(f.readlines()):
        s =  map(int,line.split(" "))
        N = s[0] #googlers
        S = s[1] #surprising
        p = s[2]
        ti = s[3:]
        
        a = "Case #%s: %s"%(i+1,solve(N,S,p,ti))
        solutions.append(a)
        print a
    
    resultFile.write("\n".join(map(str,solutions)))

    resultFile.close()
    f.close()

if __name__ == "__main__":
    while True:
        print "Input filename to solve:"
        fileNameToSolve = raw_input()
        processFile(fileNameToSolve)

        print "Results have been written to result.txt"
