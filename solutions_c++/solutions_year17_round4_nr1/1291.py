//
//  main.cpp
//  A
//
//  Created by Max Piskunov on 5/13/17.
//  Copyright © 2017 Max Piskunov. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <string>

// GMP (https://gmplib.org)
#include <gmpxx.h>

#define filename "A-large"

using namespace std;

struct input {
    int groupCount;
    int pieces;
    vector<int> groupSizes;
};

struct output {
    int freshCount;
};

void read(ifstream &in, input &test) {
    in >> test.groupCount >> test.pieces;
    test.groupSizes.resize(test.groupCount);
    for (int i = 0; i < test.groupCount; i++) {
        in >> test.groupSizes[i];
    }
}

void write(ofstream &out, output test) {
    out << test.freshCount;
}

output solve (input test) {
    output result;
    result.freshCount = 0;
    
    if (test.pieces == 2) {
        int evenCount = 0;
        int oddCount = 0;
        for (int i = 0; i < test.groupCount; i++) {
            if (test.groupSizes[i] % 2 == 0) evenCount++;
            else oddCount++;
        }
        result.freshCount = evenCount + (oddCount + 1) / 2;
    }
    
    else if (test.pieces == 3) {
        int evenCount = 0;
        int oneCount = 0;
        int twoCount = 0;
        for (int i = 0; i < test.groupCount; i++) {
            if (test.groupSizes[i] % 3 == 0) evenCount++;
            else if (test.groupSizes[i] % 3 == 1) oneCount++;
            else twoCount++;
        }
        result.freshCount += evenCount;
        int common = min(oneCount, twoCount);
        result.freshCount += common;
        oneCount -= common;
        twoCount -= common;
        int nonCommon = max(oneCount, twoCount);
        result.freshCount += (nonCommon + 2) / 3;
    }
    
    else if (test.pieces == 4) {
        int evenCount = 0;
        int oneCount = 0;
        int twoCount = 0;
        int threeCount = 0;
        for (int i = 0; i < test.groupCount; i++) {
            if (test.groupSizes[i] % 4 == 0) evenCount++;
            else if (test.groupSizes[i] % 4 == 1) oneCount++;
            else if (test.groupSizes[i] % 4 == 2) twoCount++;
            else if (test.groupSizes[i] % 4 == 3) threeCount++;
        }
        
        result.freshCount += evenCount;
        result.freshCount += twoCount / 2;
        twoCount = twoCount % 2;
        int common = min(oneCount, threeCount);
        result.freshCount += common;
        oneCount -= common;
        threeCount -= common;
        int nonCommon = max(oneCount, threeCount);
        if (twoCount == 1) nonCommon += 2;
        result.freshCount += (nonCommon + 3) / 4;
    }
    
    return result;
}

void readAll(vector <input> &tests) {
    ifstream in("/Users/maxitg/Downloads/" + (string)filename + ".in.txt");
    
    int T;
    in >> T;
    tests.resize(T);
    for (int i = 0; i < T; i++) {
        read(in, tests[i]);
    }
    
    in.close();
}

void writeAll(vector <output> &results) {
    ofstream out("/Users/maxitg/Downloads/" + (string)filename + ".out.txt");
    
    out << "Case #1: ";
    write(out, results[0]);
    for (int i = 1; i < results.size(); i++) {
        out << endl << "Case #" << i+1 << ": ";
        write(out, results[i]);
    }
    
    out.close();
}

void solveAll(vector <input> &tests, vector <output> &results) {
    results.resize(tests.size());
    for (int i = 0; i < tests.size(); i++) results[i] = solve(tests[i]);
}

int main(int argc, const char * argv[]) {
    vector <input> tests;
    vector <output> results;
    
    readAll(tests);
    solveAll(tests, results);
    writeAll(results);
    
    return 0;
}
