'''
Created on Apr 3, 2017

@author: cmahl_000
'''
import time

class CodeJam:
    
    def problem1(self, inputInt):
        start = time.time()
        original = inputInt
        array = []
        x = 1
        if inputInt == 0:
            return "INSOMNIA"
        while len(array) < 10:
            temp = inputInt
            while temp > 0:
                digit = temp % 10
                if not (self.search(digit, array)):
                    array.append(digit)
                    print(temp)
                    temp = temp // 10
                    print(temp)
                            
            x +=1
            inputInt = original * x
            if (time.time() - start) > 1:
                return "INSOMNIA" 
        
        return inputInt - original
    
    def OverProblem1(self):
        cases = int(input())
        for i in range(cases):
            k = int(input())
            print("Case #" + str(i+1) + ": " + str(self.problem1(int(input()))))
            
        
        
    def search(self, int, array):
        for i in array:
            if int == i:
                return True
        return False
    
    def reverse(self, string):
        if len(string) == 0:
            return ""
        return self.reverse(string[1:]) + string[0:1]
    
    def num2(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            return 3
        return self.num2(n-1) + self.num2(n-2) + self.num2(n-3)
    
    def num3(self, n):
        if n == 0:
            return 0
        return n + self.num3(n-1)
    
    def num4(self, list):
        if len(list) == 1:
            return list[0]
        return self.helpNum4(list[:len(list) - 1], list[len(list)-1])
    
    def helpNum4(self, list, compare):
        if len(list) == 1:
            if list[0] > compare:
                return list[0]
            return compare
        newMax = self.helpNum4(list[:len(list) - 1], list[len(list) - 1])
        if compare > newMax:
            return compare
        return newMax
    
    def num5(self, list):
        count = self.helpNum5(list, 0)
        return count
    
    def helpNum5(self, list, count):
        if len(list) == 0:
            return count
        if list[0] == 1:
            return self.helpNum5(list[1:], count + 1)
        return self.helpNum5(list[1:], count)
    
    def num6(self, string):
        if len(string) == 0:
            return True
        if len(string) == 1:
            return True
        if string[0] != string[len(string) - 1]:
            return False
        return self.num6(string[1:len(string) - 1])
    
    def oneb1(self):
        numOfCases = int(input())
        print("Number of Cases is " + str(numOfCases))
        for i in range(numOfCases):
            newInput = input().split()
            distance = int(newInput[0])
            numOfHorses = int(newInput[1])
            largestTime = 0
            for k in range(numOfHorses):
                input2 = input().split()
                toGo = distance - int(input2[0])
                time = toGo / int(input2[1])
                if time > largestTime:
                    largestTime = time
            print("Case #" + str(i+1) + ": " + str(distance/largestTime))

if __name__ == "__main__":
    code = CodeJam()
    code.oneb1()
    
    
    
    
    
    
    