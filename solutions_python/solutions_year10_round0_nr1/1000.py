'''Code for Google Code Jam 2010, Snapper Chain problem'''


class Snapper():

    def __init__(self, state):
        self.on = state
        
    def toggleOn(self):
        self.on = (self.on ^ 1)
        
    def getOn(self):
        return self.on


def allPrevOn(list, index):
    if index == 0:
        return 1
    if list[index-1] == 0:
        return 0
    else:
        return allPrevOn(list, index-1)


def main():
    
    filename = raw_input("File name?: ") #get the file from the user
    myfile = file(filename)
    numCases = int(myfile.readline()) #get the number of cases
    
    '''Get the number of trips and the times of the trips from the file'''
    for case in range(numCases):
        [N, K] = myfile.readline().split()
        N = int(N)
        K = int(K)
        '''
        snappers = []
        newsnappers = []
        for i in range(N):
            snappers.append(0)
            newsnappers.append(0)
        
        
        for i in range(K):
            for j in range(N):
                if allPrevOn(snappers, j):
                    newsnappers[j] = 1^snappers[j]
                    print str(j) +":"+str(snappers[j])
            for j in range(N):
                snappers[j] = newsnappers[j]
            print str(i) + ": " + str(snappers)
        
        '''
        littlek = 0
        for i in range(N):
            littlek = littlek*2+1
        
        diff = K-littlek
        
        if K == 0:
            result = "OFF"
        elif diff == 0 or diff%(littlek+1)==0:
            result = "ON"
        else:
            result = "OFF"
        
        print "Case #" + str(case+1) + ": " + result


if __name__ == "__main__" : main()    


