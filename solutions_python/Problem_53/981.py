'''
Created on 08/05/2010

@author: Administrator
'''
import GoogleIO
import snapper

if __name__ == '__main__':
   
    cases = {}
    IO = GoogleIO.googleIO()
    #get the data from file
    (numOfCases,cases)=IO.getInput()
    
    for n in range(0, numOfCases):
        (numOfSnappers,numOfSwitches)=cases[n]
        snaper = snapper.SnapperClass(int(numOfSnappers))
        snaper.switcher(int(numOfSwitches))
        
        if snaper.checkLight()==True :
            output ="Case #%d: %s" % (n+1,"ON")
        else:
            output ="Case #%d: %s" % (n+1,"OFF")
            
        IO.writeOutput(output)