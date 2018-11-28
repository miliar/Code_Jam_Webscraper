#!/usr/env python
#

import re
import sys
import copy


class SystemState:
    def __init__(self,time,cookies,rate):
        self.time = time
        self.cookies = cookies
        self.rate = rate
    def addFarm(self,farm_rate):
        self.rate += farm_rate
    

class Solver:
    def __init__(self,C,F,X):
        self.farm_cost = C
        self.farm_gains = F
        self.win_amount = X
        
    def runScenario(self,state,action):
        if action == "build_farm":
            time_to_farm = (self.farm_cost - state.cookies)/state.rate
            state.addFarm(self.farm_gains)
            time0 = state.time + time_to_farm + (self.win_amount/state.rate)
            return time0
        else:
            return state.time + (self.win_amount/state.rate)
        
    def nextNodeTime(self,state):
        time_to_farm = (self.farm_cost - state.cookies)/state.rate
        return state.time + time_to_farm
    
    def solveProblem(self):
        max = self.win_amount/2.0
        done = False
        time = 0
        while not done:
            
            state = SystemState(0.0,0.0,2.0)
            while (time < max): 
                time = max
                state0 = copy.deepcopy(state)
                state1 = copy.deepcopy(state)

                time_farm = self.runScenario(state0, "build_farm")
                time_wait = self.runScenario(state1, "wait")

                
                if time_farm < time_wait:
                    time = self.nextNodeTime(state)
                    rate = state.rate + self.farm_gains
                    state = SystemState(time,0.0,rate)
                else:
                    done = True
                    time = time_wait
                    break
        return time
                    
                
        
        
        
def solveCases(inputfile):
    filein = open(inputfile)
    
    lines = filein.readlines()
    
    number_of_cases = int(lines[0])
    
    for case_num in range(1,number_of_cases+1):
        case_values = re.split(' ', lines[case_num].strip())

        s = Solver(float(case_values[0]),float(case_values[1]),float(case_values[2]))
        result = s.solveProblem()
        
        print "Case #" + str(case_num) + ": " + str(result)
        
if __name__ == "__main__":
    solveCases(sys.argv[1])

