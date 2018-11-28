//
//  main.cpp
//  C
//
//  Created by Max Piskunov on 4/7/17.
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

#define filename "C-large"

using namespace std;

struct input {
    int64_t stalls;
    int64_t people;
};

struct output {
    int64_t max;
    int64_t min;
};

void read(ifstream &in, input &test) {
    in >> test.stalls >> test.people;
}

void write(ofstream &out, output test) {
    out << test.max << " " << test.min;
}

vector<int64_t> split (int64_t stalls) {
    vector<int64_t> result;
    result.resize(2);
    result[1] = (stalls - 1) / 2;
    result[0] = stalls - 1 - result[1];
    return result;
}

vector<int64_t> splits (int64_t people, int64_t stalls) {
    if (people == 1) {
        return split(stalls);
    } else {
        vector<int64_t> currentSplit;
        currentSplit = split(stalls);
        people--;
        if (people % 2 == 1) {
            return splits((people + 1) / 2, currentSplit[0]);
        } else {
            return splits((people + 1) / 2, currentSplit[1]);
        }
    }
}

output solve (input test) {
    output result;
    int64_t currentPeople = test.people;
    int64_t currentStalls = test.stalls;
    vector<int64_t> last;
    
    last = splits(currentPeople, currentStalls);
    
    result.max = last[0];
    result.min = last[1];
    
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
