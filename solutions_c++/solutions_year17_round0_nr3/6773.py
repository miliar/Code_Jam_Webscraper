//
//  main.cpp
//  GoogleCodeJam2017
//
//  Created by Julia Tazin on 3/30/17.
//  Copyright © 2017 Julia Tazin. All rights reserved.
//

/*-----------------------------
 "Literature"
 http://www.cplusplus.com/reference/string/stoi/
 ----------------------------*/

/*-----------------------------
 Notes
 1) Everything is 0-indexed (except the case numbers in the output).
 
 a) Input usually has first n lines with meta information
 b) Several cases follow, each of which can span multiple lines
 
 3) Command line tool available for downloading/submitting.
 ----------------------------*/

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

/*-----------------------------
 Input/Output File Paths
 ----------------------------*/
const string pathToInputOutputDirectories = "/Users/Julia/Documents/Julia's Documents/Programming Projects/GoogleCodeJam/GoogleCodeJam2017/";
const string pathToInputDirectory = "GoogleCodeJam2017InputFiles/";
const string pathToOutputDirectory = "GoogleCodeJam2017OutputFiles/";

// TODO_1: Specify the problem identifier.
const string currentProblemIdentifier = "C-small-1-attempt0";

const string inputFileExtension = ".in";
const string outputFileExtension = ".out";

const string fullPathToInputFile = pathToInputOutputDirectories + pathToInputDirectory + currentProblemIdentifier + inputFileExtension;
const string fullPathToOutputFile = pathToInputOutputDirectories + pathToOutputDirectory + currentProblemIdentifier + outputFileExtension;

/*-----------------------------
 Globals
 ----------------------------*/

// TODO_?:

/*-----------------------------
 Helper Types
 ----------------------------*/

typedef enum _lineType
{
    intLine,
    intArrayLine,
    stringLine,
    stringArrayLine,
    charArrayLine,
    customLine
} lineType;

typedef enum _direction
{
    north = 0,
    east = 1,
    south = 2,
    west = 3
} direction;

/*-----------------------------
 Input/Output Classes
 ----------------------------*/

class inputClass
{
public:
    int GetNumberOfCasesFromInputFile(ifstream &inputFile); // Generic*: Returns the number of cases in the file. *Used when the first line represents the number of cases only. *Must be called before any lines are read.
    void ReadCaseInputFromFile(ifstream &inputFile); // Semi-generic*: Given a file, will read a case and fill out the class variables. *Must be edited to contain class variable names.
    void* ParseLine(string &line, lineType lineType, int numberOfElementsInLine); // Generic*: Will parse a line according to its lineType. *Only supports a handful of speciic line types
    void CustomParseLine(string &line);
    string FindTheMeatOfTheProblem(); // Specific: Solves the problem. Bulk of the work is here. Returns a properly formatted string without the "Case #n: ".
    void FreeMemory(); // Semi-generic*: Frees class memory. *Need to specify which class variables must be freed and how.
    
    // TODO_2: How many lines per case?
    static const int numberOfLinesPerCase = 1;
    // TODO_3: What are the input line types?
//    lineType inputLineTypes[numberOfLinesPerCase] = {intArrayLine};
    
    // TODO_4: What class variables are needed? (Typically, a single input line corresponds to a class variable.)
    long numberOfUserStallsN;
    long numberOfPeopleK;
    
    // TODO: delete for next problem
    
    
    // TODO_: Class variables not directly on an input line
};

class outputClass
{
public:
    void WriteCaseOutputToFile(ofstream &outputFile, int caseNumber, string output); // Generic: ????
//    bool Test(string output);
    
//    int outputCaseType = intArrayLine; // TODO: needed?
};

/*-----------------------------
 File Parsing
 ----------------------------*/
vector<string> &split(const string &s, char delim, vector<string> &elems) {
    stringstream ss(s);
    string item;
    while (getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}

vector<string> split(const std::string &s, char delim) {
    vector<string> elems;
    split(s, delim, elems);
    return elems;
}

int inputClass::GetNumberOfCasesFromInputFile(ifstream &inputFile)
{
    string line;
    if (getline(inputFile, line))
    {
        return stoi(line);
    }
    
    return -1;
}

void inputClass::ReadCaseInputFromFile(ifstream &inputFile)
{
    string line;
    if (getline(inputFile, line))
    {
        vector<string> splitLine;
        splitLine = split(line, ' ');
        // TODO_B: comment out assert
//        if (splitLine.size() != 2)
//        {
//            cout << "Incorrect assumption!!\n";
//        }
        numberOfUserStallsN = stol(splitLine[0]);
//        cout << "Number of user stalls N: "+ to_string(numberOfUserStallsN) + "\n"; // TODO_B: comment out for perf
        numberOfPeopleK = stol(splitLine[1]);
//        cout << "Number of people K: "+ to_string(numberOfPeopleK) + "\n"; // TODO_B: comment out for perf
    }

}

void outputClass::WriteCaseOutputToFile(ofstream &outputFile, int caseNumber, string output)
{
    outputFile << "Case #" + to_string(caseNumber) + ": " + output + "\n";
}

/*-----------------------------
 Helper functions
 ----------------------------*/
typedef std::vector<int> ints;

void insert(vector<long> &vectorOfLongs, long valueToInsert) {
    vector<long>::iterator it = lower_bound(vectorOfLongs.begin(), vectorOfLongs.end(), valueToInsert, greater<long>()); // Find proper position in descending order
    vectorOfLongs.insert(it, valueToInsert); // Insert before iterator it.
}

/*-----------------------------
 The Meat of the Problem
 ----------------------------*/
string inputClass::FindTheMeatOfTheProblem()
{
    // TODO_: Solve the problem!
    string returnString;
    
    // Let's start our sorted (from greatest to least) vector of stall clusters.
    vector<long> sortedStallClusters(1,numberOfUserStallsN);
    
    long farthestNeighborDistance = 0;
    long closestNeighborDistance = 0;
    
    // Now let's iterate as many times as there are people.
    for (long i = 0; i < numberOfPeopleK; i++)
    {
        // The max cluster should be represented by the first number in the vector, since we keep it sorted.
        long maxClusterSize = sortedStallClusters[0];
        
        // Let's split the cluster size into farthest and closest neighbor distances.
        if (maxClusterSize % 2 == 0)
        {
            // The cluster size is even.
            farthestNeighborDistance = (maxClusterSize / 2);
            closestNeighborDistance = (maxClusterSize / 2) - 1;
        }
        else
        {
            // The cluster size is odd.
            farthestNeighborDistance = (maxClusterSize - 1) / 2;
            closestNeighborDistance = (maxClusterSize - 1) / 2;
        }
        
        // Let's remove our old cluster and do a sorted insert of these distances into the array.
        sortedStallClusters.erase (sortedStallClusters.begin());
        insert(sortedStallClusters, closestNeighborDistance);
        insert(sortedStallClusters, farthestNeighborDistance);
    }
    
    // We want to return farthestNeighborDistance and closestNeighborDistance.
    returnString = to_string(farthestNeighborDistance) + " " + to_string(closestNeighborDistance);
    
//    cout << "Return string: "+ returnString + "\n"; // TODO_B: comment out for faster perf
    return returnString;
}

/*-----------------------------
 Main
 ----------------------------*/

void MainAlgorithm()
{
    inputClass inputObject;
    outputClass outputObject;
    
    // Open input file and get number of cases.
    ifstream inputFile;
    inputFile.open(fullPathToInputFile);
    int numberOfCases = inputObject.GetNumberOfCasesFromInputFile(inputFile);
    
    // Prepare output file.
    ofstream outputFile;
    outputFile.open(fullPathToOutputFile);
    
    // For each set of data, compute the answer.
    for (int i = 0; i < numberOfCases; i++)
    {
//        cout << "Calculating Case #"+ to_string(i + 1) + "\n"; // TODO_B: comment out for faster perf
        // Read case from the file.
        inputObject.ReadCaseInputFromFile(inputFile);
        
        // Run algorithm on set of data.
        string output = inputObject.FindTheMeatOfTheProblem();
        
        //        // Test output.
        //        outputObject.Test(output);
        
        // Write output results for set to file.
        outputObject.WriteCaseOutputToFile(outputFile, i + 1, output);
    }
    
    inputFile.close();
    outputFile.close();
    
    cout << "Done!\n";
}

int main(int argc, const char * argv[])
{
    cout << "Hello, World!\n";
    
    MainAlgorithm();
    
    return 0;
}


