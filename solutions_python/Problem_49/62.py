import sys

class Plant(object):
    
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        
    def __str__(self):
        return "[" + str(self.x) + ", "+ str(self.y) + ", " + str(self.r) + "]"

class Sprinkler(list):
    
    def __init__(self, name):
        self.name = name
        
    def radius(self):
        diameter = 0
        for plant1 in self:
            for plant2 in self:
                diameter= max(diameter, distance(plant1, plant2))
        return diameter / 2
    
    def __str__(self):
        return self.name + " -" + ', '.join([str(plant) for plant in self])


def distance(plant1, plant2):
    return ((plant1.x -plant2.x)**2 + (plant1.y -plant2.y)**2)**0.5 + plant1.r + plant2.r
        

def get_tests():
    tests = []
    input_file = open(sys.argv[1])
    case_numbers = int(input_file.readline().strip())
    for case_number in range(case_numbers):
        plants = int(input_file.readline().strip())
        rows = []
        for row in range(plants):
            columns = input_file.readline().strip()
            rows.append(columns)
        tests.append(rows)
    return tests

def solve(test):
    plants = []
    for row in test:
        x,y,r = row.split()
        plant = Plant(int(x),int(y),int(r))
        plants.append(plant)
    
    radius = 1000
    for plant in plants:
        radius = min(radius,solve_for_plant(plant, plants))
    return radius

def solve_for_plant(plant, plants):
    sprinkler1 = Sprinkler("Sprinkler 1")
    sprinkler1.extend(plants)
    sprinkler2 = Sprinkler("Sprinkler 2")
    minimum_radius = 1001
    ordered_plants = order_by_distance(plant, plants)
    while sprinkler1.radius() > sprinkler2.radius() and len(ordered_plants) > 0:
        move_plant = ordered_plants.pop()
        if move_plant == plant:
            pass
        else:
            sprinkler1.remove(move_plant)
            sprinkler2.append(move_plant)
        minimum_radius = min(minimum_radius, max(sprinkler1.radius(),sprinkler2.radius()))
    #print minimum_radius
    return minimum_radius
        
def order_by_distance(plant, plants):
    ordered = []
    original = []
    original.extend(plants)
    while len(original) > 0:
        ordered_plant = get_most_distant_plant(plant, original)
        original.remove(ordered_plant)
        ordered.append(ordered_plant)
    ordered.reverse()
    return ordered
        
        
    
def get_most_distant_plant(plant, plants):
    most_distant = None
    most_distant_distance = 0
    for other_plant in plants:
        dist = distance(plant, other_plant)
        if dist > most_distant_distance:
            most_distant_distance = dist
            most_distant = other_plant
    #print most_distant, most_distant_distance
    return most_distant
            
tests = get_tests()
index = 1
for test in tests:
    value = solve(test)
    print "Case #" + str(index)+ ": " + str(value)
    index = index +1