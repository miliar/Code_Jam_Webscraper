import sys

def stand_up(cases, max_shy, people):
    """
    this method finds out how many friedns need to be invited 
    and return this number
    """
    #nr_and_shylevel er ein string der første digit tal folk med shynesslevel 0, andre er shynesslevel 1, osb
    #må for kvart tal kunna sjekka om det er nok folk som har reist seg for at dei siste skal greia å reisa seg
    #maa ha folk på plass 1 for å faa alt i gong. etter det er det tal folk som har reist seg som tel
    
    standing = 0
    needed = 0
    
    #dersom det er folk med nivå ein, og det alt står nokon, reiser desse seg og
    for i in range(len(people)):
        #dersom nok folk alt står (inkludert needed), reiser resten seg
        if i > standing+needed:
            needed = i-standing
        standing += int(people[i])
    return standing, needed


def input_information():
    """
    this method lets user write in information
    """
    #tek ut tal linjer i første metoden
    line = sys.stdin.readline().split()
    cases = int(line[0])
    for i in range(cases):
        max_shy = int(line[i*2+1])
        people = str(line[i*2+2])
        standing, needed = stand_up(cases, max_shy, people)
        print("Case #"+str(i+1)+": "+str(needed))
        
        
        
        
        
        
        
        
        
        
        
    
    