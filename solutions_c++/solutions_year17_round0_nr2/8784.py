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
const string currentProblemIdentifier = "B-large";

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
    long largestNumberN;
    
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
//vector<string> &split(const string &s, char delim, vector<string> &elems) {
//    stringstream ss(s);
//    string item;
//    while (getline(ss, item, delim)) {
//        elems.push_back(item);
//    }
//    return elems;
//}
//
//vector<string> split(const std::string &s, char delim) {
//    vector<string> elems;
//    split(s, delim, elems);
//    return elems;
//}

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
        largestNumberN = stol(line);
//        cout << "Here is my numbah: "+ to_string(largestNumberN) + "\n";
    }

}

void outputClass::WriteCaseOutputToFile(ofstream &outputFile, int caseNumber, string output)
{
    outputFile << "Case #" + to_string(caseNumber) + ": " + output + "\n";
}

/*-----------------------------
 Helper functions
 ----------------------------*/


/*-----------------------------
 The Meat of the Problem
 ----------------------------*/
string inputClass::FindTheMeatOfTheProblem()
{
    // TODO_: Solve the problem!
    string returnString;
    
    int maxNumberOfDigits = 20; // We have at most 19 digits
    int* array = new int[maxNumberOfDigits];
    
    // Zero it out.
    for (int i = 0; i < maxNumberOfDigits; i++)
    {
        array[i] = 0;
    }

    int arrayIndex = 19; // the array index
//    cout << "Here is our largestNumberN: "+ to_string(largestNumberN) + "\n";
    while (largestNumberN) // Loop till there's nothing left.
    {
        array[arrayIndex] = largestNumberN % 10; // Assign the last digit.
        largestNumberN = largestNumberN / 10; // Right shift the number.
        arrayIndex--;
    }
    int lastLeadingZeroDigit = arrayIndex;
    
    // Let's find the first digit that doesn't hold to the tidy property.
    bool numberIsTidy = true;
    arrayIndex = (lastLeadingZeroDigit + 1);
    while (numberIsTidy && (arrayIndex <= (maxNumberOfDigits - 2)))
    {
        if (array[arrayIndex] > array[arrayIndex + 1])
        {
            // Found a digit that doesn't hold.
            numberIsTidy = false;
            break;
        }
        
        arrayIndex++;
    }
    
    if (numberIsTidy == false)
    {
        // This number isn't tidy.
        // Let's see if decreasing this current digit by 1 doesn't require any processing for the preceding rest.
        bool foundOurPivot = false;
        while ((!foundOurPivot) && (arrayIndex >= lastLeadingZeroDigit + 2))
        {
            // TODO: comment out this assert
//            if (array[arrayIndex] == 0)
//            {
//                cout << "Incorrect assumption!!!\n";
//            }
            
            if ((array[arrayIndex] - 1) >= array[arrayIndex - 1]) // The decreased-by-one value should still be greater or equal to the preceding. If so, we can end processing.
            {
                foundOurPivot = true;
                array[arrayIndex] = array[arrayIndex] - 1;
                break;
            }
            
            // Otherwise, we need to keep searching for our pivot
            arrayIndex--;
        }
        
        if (!foundOurPivot)
        {
            // If we still haven't found our pivot, it must be our first digit. We do this separately, since we have nothing to compare our first digit to.
            // TODO: comment out this assert
//            if (arrayIndex != lastLeadingZeroDigit + 1)
//            {
//                cout << "Incorrect assumption!!!\n";
//            }
            
            array[arrayIndex] = array[arrayIndex] - 1;

        }
        
        // Now nine out the rest.
        for (arrayIndex = arrayIndex + 1; arrayIndex < maxNumberOfDigits; arrayIndex++)
        {
            array[arrayIndex] = 9;
        }
    }
    
    long outputNumber = 0;
    for (arrayIndex = 0; arrayIndex < maxNumberOfDigits; arrayIndex++)
    {
        outputNumber = outputNumber * 10;
        outputNumber = outputNumber + array[arrayIndex];
    }
    
//    cout << "Here is our outputNumber: "+ to_string(outputNumber) + "\n";
    returnString = to_string(outputNumber);
    
    delete [] array;
    array = NULL;
    
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
//        cout << "Calculating Case #"+ to_string(i + 1) + "\n"; // TODO: comment out for faster perf
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


