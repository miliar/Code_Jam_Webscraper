//
//  main.cpp
//  IHOP
//
//  Created by Anirudh Mendiratta on 4/8/17.
//  Copyright © 2017 anirudh. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <queue>
#include <utility>
#include <algorithm>
#include <ctime>

using namespace std;

typedef long long int int64;
typedef unordered_map<string, int64> NodeDistanceMap;
typedef pair<string, int> NodeDistancePair;

void printVector(vector<string> inputVector)
{
    for(size_t i=0; i<inputVector.size(); i++)
    {
        cout << inputVector[i] << endl;
    }
}

int numberOfMinuses(string inputString)
{
    int result = 0;
    for(size_t i=0; i<inputString.size(); i++)
    {
        if(inputString[i] == '-') { result++; }
    }
    return result;
}

string flip(string inputString, int startIndex, int numToFlip)
{
    string outString = inputString;

    for(size_t i=startIndex;
        (i<startIndex + numToFlip) && (i<outString.size());
        i++)
    {
        if(outString[i]=='+')
        {
            outString[i] = '-';
        }
        else if(outString[i] == '-')
        {
            outString[i] = '+';
        }
    }
    return outString;
}

vector<string> childrenOf(string node, int k)
{
    vector<string> children(node.size()-k+1);
    for(size_t i=0; i < node.size() - k + 1; i++)
    {
        children[i] = flip(node, static_cast<int>(i), k);
    }
    return children;
}

int64 shortestPathToHappiness(string source, int k)
{
    string destination(source.size(), '+');
    if(source == destination)
    {
        return 0;
    }
    queue<string> nodes;
    NodeDistanceMap visitedNodes;
    nodes.push(source);
    visitedNodes[source] = 0;
    bool foundTarget = false;
    while(!nodes.empty())
    {
        string currentNode = nodes.front();
        nodes.pop();
        //cout << "The queue size is " << nodes.size() << endl;
        vector<string> children = childrenOf(currentNode, k);
        for(size_t i=0; i<children.size(); i++)
        {
            string currentChild = children[i];

            if(visitedNodes.find(currentChild) != visitedNodes.end() &&
               (visitedNodes[currentChild] < visitedNodes[currentNode]+1))
            {
                // Node already exists in map with lesser distance
                
                continue;
            }
            else
            {
                visitedNodes[currentChild] = visitedNodes[currentNode] + 1;
                if(currentChild == destination)
                {
                    foundTarget = true;
                    break;
                }
            }

            nodes.push(currentChild);
            //cout << "The queue size is " << nodes.size() << endl;
        }
        if(foundTarget)
        {
            break;
        }
    }
    
    if(visitedNodes.find(destination) != visitedNodes.end())
    {
        return visitedNodes[destination];
    }
    return -1;
}




int main(int argc, const char * argv[]) {
    // insert code here...
    
    size_t numTestCases;
    cin >> numTestCases;
    
    vector<string> pancakes(numTestCases);
    vector<int> K(numTestCases);
    
    for(size_t i=0; i<numTestCases; i++)
    {
        string Kstr;
        cin >> pancakes[i] >> Kstr;
        K[i] = stoi(Kstr);
    }
    
    for(size_t i=0; i<numTestCases; i++)
    {
        int64 shortestPath = shortestPathToHappiness(pancakes[i], K[i]);
        cout << "Case #" << i+1 << ": ";
        if(shortestPath == -1)
        {
            cout << "IMPOSSIBLE" << endl;
        }
        else
        {
            cout << shortestPath << endl;
        }
    }
    
    return 0;
}
