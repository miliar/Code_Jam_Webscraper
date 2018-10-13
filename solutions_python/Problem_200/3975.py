import math

class Stall:
    
    def __init__(self, index, n):
        
        self.occupied = False
        self.index = index + 1
        self.right = n + 1
        self.left = 0
        self.ls = (self.index - self.left) - 1
        self.rs = (self.right - self.index) - 1
        self.mini = 0
        self.maxi = 0
        
    def getIndex(self):
        return self.index
    
    def occupy(self):
        self.occupied = True
    
    def isOccupied(self):
        return self.occupied
        
    def updateLeft(self, newLeft):
        self.left = newLeft + 1
        self.ls = (self.index - self.left) - 1
        
    def updateRight(self, newRight):
        self.right = newRight + 1
        self.rs = (self.right - self.index) - 1
        
    def min(self):
        if self.ls <= self.rs:
            return self.ls
        return self.rs
    
    def max(self):
        if self.ls >= self.rs:
            return self.ls
        return self.rs
    



class Google:
    
    def toArray(self, number):
        string = str(number)
        array = [d for d in string]
        return array
    
    def arrayToNumber(self, array, firstNumber):
        string = ""
        for i in range(firstNumber, len(array)):
            string += array[i]
        return int(string)
    
    def sameNumber(self, number, length):
        string = ""
        for i in range(length):
            string = string + str(number)
        return int(string)

    def isIncreasing(self, number):
        array = self.toArray(number)
        if len(array) < 2:
            return str(number)
        if int(number) >= self.sameNumber(int(array[0]), len(array)):
            
            return array[0] + self.isIncreasing(self.arrayToNumber(array, 1))
        string = ""
        string += str(int(array[0]) - 1)
        for i in range(1, len(array)):
            string += "9"
        return string
    
    def bigProblem(self, number):
        return int(self.isIncreasing(number))
    
    def bathroom(self, n, k):
        if n == k:
            return "0 0"
        if k == 1:
            return str(n/2) + " " + str(n/2 -1)
        if k == 2:
            if n % 4 == 0 or n % 4 == 1:
                return str(n//4) + " " + str(n//4 - 1)
            return str(n//4) + " " + str(n//4) 
        self.stalls = [None] * n
        for i in range(n):
            self.stalls[i] = Stall(i, n)
        
        for i in range(k):
            if i != (k - 1):
                self.placePerson(n)
                print(str(i))
            else:
                lastPlace = self.placePerson(n)
                return str(self.stalls[lastPlace].max()) + " " + str(self.stalls[lastPlace].min())
    
    def placePerson(self, n):
            
        array = []
        
        max1 = -1
        for i in range(n):
            if self.stalls[i].isOccupied():
                pass
            elif self.stalls[i].min() > max1:
                array = []
                array.append(i)
                max1 = self.stalls[i].min()
            elif self.stalls[i].min() == max1:
                array.append(i)
        
        if len(array) == 1:
            self.stalls[array[0]].occupy()
            self.updateStalls(array[0], n)
            return array[0]
        placer = -1
        if len(array) > 1:
            max2 = -1
            for i in array:
                if self.stalls[i].max() > max2:
                    max2 = self.stalls[i].max()
                    placer = i
        self.stalls[placer].occupy()
        self.updateStalls(placer, n)
        return placer
                    
    
    def updateStalls(self, index, n):
        leftward = index - 1
        rightward = index + 1
        while leftward >= 0 and not self.stalls[leftward].isOccupied():
            self.stalls[leftward].updateRight(index)
            leftward -= 1
        while rightward < (n) and not self.stalls[rightward].isOccupied():
            self.stalls[rightward].updateLeft(index)
            rightward += 1
    
    def daddy(self):
        cases = int(input())
        k = 0
        for i in range(cases):
            k = input()
            print("Case #" + str(i+1) +  ": " + str(self.bigProblem(k)))

        
                
            
if __name__ == "__main__":
    google = Google()
    google.daddy()
