'''
Created on 08/05/2010

@author: Administrator
'''
import GoogleIO
class Ride(object):
    '''
    classdocs
    '''

    numOfRidesInQueue=0
    def __init__(self):
        '''
        Constructor
        '''
        self.numOfRidesInQueue=0
    
    
    def  useRide(self,groups,space,numOfRides):
        localSum=0
        n=0
        sum=0
        notEnoughPeople=False
        
        for i in range(0,numOfRides):
            while localSum<space:
                try:
                    localSum=localSum+groups[n]
                    n=n+1
                except:
                    n=0
                    if i==0:
                        notEnoughPeople = True
                        break
                    else:
                        if notEnoughPeople==True:
                            break
                        else:
                            localSum=localSum+groups[n]
                            n=n+1
                
            if localSum>space:
                localSum=localSum-groups[n-1]
                n=n-1
            
            sum=sum+localSum
            localSum=0
        return sum
    

if __name__ == "__main__":
    
    cases = {}
    intgroups=[]
    park = Ride()
    IO = GoogleIO.googleIO()
    #get the data from file
    (numOfCases,cases)=IO.getInput()
    for n in range(0, numOfCases):
        (numOfRides,space,numOfGroups,groups)=cases[n]
        for group in groups:
            intgroups.append (int(group))
        
        sum=park.useRide(intgroups,int(space),int(numOfRides))  
        intgroups=[]
        output ="Case #%d: %d" % (n+1,sum)
        IO.writeOutput(output)
    
    
    
   # groups=(2,4,2,3,4,2,1,2,1,3)*100
    
   # sum=park.useRide(groups,5,10000)
    #print sum
    