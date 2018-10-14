import os
import sys
import pdb
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

file = open('input.txt')
input = file.read()
file.close()

input = input.split('\n')
T = int(input[0])
input = input[1:]

expected_value = []
passwords = []
class password:
    A, B = 1, 1
    prob = []
    probability = 1
    def opt1(self):
        probability = 1.0
        for i in range(0,self.A):
            probability *= self.prob[i]
        #pdb.set_trace()
        return (probability * (self.B-self.A+1) + (1-probability)*(self.B-self.A+1+self.B+1))
    def opt2(self):
        probability = 1.0
        minimum = 10000000
        for i in range(1,self.A+1):
            probability = 1.0
            for j in range(0,self.A-i):
                probability *= self.prob[j]
            minimum = min(minimum, i + (probability * (self.B-self.A+i+1) + (1-probability) * (self.B-self.A+i+1+self.B+1)) )
        return minimum
    def opt3(self):
        return self.B+2
    
for i in range(0,T):
    passwords += [password()]
    passwords[i].prob = []
    passwords[i].A = int(input[0].split(' ')[0])
    passwords[i].B = int(input[0].split(' ')[1])
    input = input[1:]
    #pdb.set_trace()
    for j in range(0,passwords[i].A):
        passwords[i].prob += [float(input[0].split(' ')[j])]
    input = input[1:]
    #pdb.set_trace()
    passwords[i].minimum_keystrokes = min(min(passwords[i].opt1(),passwords[i].opt2()),passwords[i].opt3())


file = open('output.txt','w')
for i in range(0,T):
    file.write('Case #'+str(i+1)+': '+str(float(passwords[i].minimum_keystrokes))+'\n')
file.close()
