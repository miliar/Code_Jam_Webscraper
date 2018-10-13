class TestCase():
    def __init__(self, distance, horses):
        self.distance = distance
        self.horses = horses
        print(distance)
        print(horses)

    def computeTime(self, horse):
        return (self.distance-horse[0])/horse[1]
        
    def solve(self):
        worst = 0
        for horse in self.horses:
            if worst < self.computeTime(horse):
                worst = self.computeTime(horse)
        return self.distance/worst
            

            


def loadTestCases(taskChar, path):
    out = []
    input_file = open(path)
    for i in range(int(input_file.readline())):
        (distance, count) = [int(i) for i in input_file.readline().split()]
        horses = []
        for i in range(count):
            horses.append([int(i) for i in input_file.readline().split()])
        out.append(TestCase(distance, horses))
    input_file.close()
    return out

def solve(path):
    tcs = loadTestCases("B", path)
    output_file = open(path[:-3]+".out", "w")
    count = 1
    for t in tcs:
        output_file.write("Case #"+str(count)+": "+str(t.solve())+"\n")
        count += 1
        
    output_file.close()

        
        
solve("A-large.in")

    
