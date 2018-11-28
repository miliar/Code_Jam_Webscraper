class Tree():
    def __init__(self, weight, feature="", trees=[]):
        self.weight = weight
        self.feature = feature
        self.trees = trees

    def decide(self, animal):
        animal.score *= self.weight
        if self.feature != "":
            if self.feature in animal.features:
                self.trees[0].decide(animal)
            else:
                self.trees[1].decide(animal)
        return animal.score

class Animal():
    def __init__(self, name, features):
        self.name = name
        self.features = features
        self.score = 1

def parse_text(text):
    line = []
    while line == []:
        line = text.pop(0).strip(" \n()").split()
    weight = float(line[0])
    try:
        feature = line[1]
        tree1 = parse_text(text)
        tree2 = parse_text(text)
        return Tree(weight, feature, [tree1, tree2])
    except:
        return Tree(weight)

input_file = open("A-large.in.txt", "r").readlines()
output_file = open("output.txt", "w")
N = int(input_file.pop(0).strip())
for x in range(N):
    output_file.write("Case #" + str(x+1) + ":\n")
    L = int(input_file.pop(0).strip())
    text = []
    for x in range(L):
        text.append(input_file.pop(0))
    tree = parse_text(text)
    A = int(input_file.pop(0).strip())
    for x in range(A):
        info = input_file.pop(0).strip().split()
        animal = Animal(info[0], info[2:])
        output_file.write(str(tree.decide(animal)) + "\n")
output_file.close()
        
