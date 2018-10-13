'''
Created on 22/05/2010

@author: Administrator
'''
import GoogleIO
class FixIt(object):
    '''
    classdocs
    '''
    Directories=[]
    createdDir=[]
    def __init__(self):
        '''
        Constructor
        '''
        self.Directories =[]
    def addDir(self,Dir):
        local_dir=""
        local_dirs=Dir.split("/")
        for dir in local_dirs:
            if dir!="":
                local_dir=local_dir+"/"+dir
                if local_dir not in self.Directories:
                    self.Directories.append(local_dir)
                    
    
    def cleanDirs(self):
        self.Directories=[]
        
        
    def countDir(self,Dir):
        mkdirCounter=0
       
        if Dir not  in self.Directories:
            local_dir=""
            mkdirCounter=0
            local_dirs=Dir.split("/")
            for dir in local_dirs:
                if dir!="":
                    local_dir=local_dir+"/"+dir
                    if local_dir not in self.Directories:
                        self.Directories.append(local_dir)
                        mkdirCounter=mkdirCounter+1
            
        return mkdirCounter
        
    
if __name__ == '__main__':
    
    counter=0
    fixer=FixIt()
    IO = GoogleIO.googleIO() 
    (numOfCases,cases)=IO.getInput()
    for n in range(0, numOfCases):
        (existingDirs,newDirs)=cases[n]
        for Dir in existingDirs:
            fixer.addDir(Dir)
        for Dir in newDirs:
            counter=counter+fixer.countDir(Dir)
        
        output ="Case #%d: %s" % (n+1,str(counter))
        IO.writeOutput(output)
        counter=0
        fixer.cleanDirs()
            
    
                
        