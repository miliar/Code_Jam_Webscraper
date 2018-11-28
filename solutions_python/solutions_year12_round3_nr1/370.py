from copy import deepcopy;
infile = open("input.txt","r");
outfile = open("out1.txt","w");
line = infile.readline();
TestCases = int(line);
testCase = 0;
class Node:
    def __init__(self,name):
        self.name = name;
        self.successors = [];
        self.successorsCopy = []
        self.noOfPaths = {};
        self.incidentEdges = []
        
def countNoOfPaths(Graph):
    for node in Graph:
        for adj in Graph[node].incidentEdges:
            Graph[adj].successors.append(node);
    
    sources = [ node for node in Graph if len(Graph[node].successors)>0]
    print sources;
    copy = deepcopy(Graph);
    for source in sources:
        Graph = deepcopy(copy);
        Graph[source].noOfPaths[source] = 1;
        queue = [source];
        while(len(queue)>0):
            currentNode = queue.pop();
            adjNodes = Graph[currentNode].successors[0:];
            for adjNode in adjNodes:
                if source not in Graph[adjNode].noOfPaths:
                    Graph[adjNode].noOfPaths[source] = Graph[currentNode].noOfPaths[source];
                    queue.append(adjNode);
                else:
                    return "Yes";
                
    return "No";

while testCase<TestCases:
    line = infile.readline();
    noOfNodes = int(line);
    nodes = {}
    for node in range(noOfNodes):
        line = infile.readline();
        fields = line.split();
        count = int(fields[0]);
        nodes[node+1]=Node(node+1);
        if count > 0:
            for i in range(count):
                nodes[node+1].incidentEdges.append(int(fields[i+1]));
    testCase+=1;
##    if testCase==25:
##        print testCase,noOfNodes
##        for node in nodes:
##            print nodes[node].incidentEdges;
    outfile.write("Case #%d: %s"%(testCase,countNoOfPaths(nodes))+"\n");
infile.close();
outfile.close();
