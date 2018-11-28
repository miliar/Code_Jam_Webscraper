//
//  main.cpp
//  A
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

#define filename "A-large"

using namespace std;

struct input {
    string cakes;
    int size;
};

struct output {
    int count;
};

void read(ifstream &in, input &test) {
    in >> test.cakes >> test.size;
}

void write(ofstream &out, output test) {
    if (test.count == -1) {
        out << "IMPOSSIBLE";
    } else {
        out << test.count;
    }
}

output solve (input test) {
    output result;
    
    result.count = 0;
    int position = 0;
    while (position + test.size <= test.cakes.length()) {
        if (test.cakes[position] == '-') {
            result.count++;
            for (int i = 0; i < test.size; i++) {
                test.cakes[position + i] = test.cakes[position + i] == '+' ? '-' : '+';
            }
        }
        position++;
    }
    
    for (int k = 0; k < test.size - 1; k++) {
        if (test.cakes[position + k] == '-') {
            result.count = -1;
            return result;
        }
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
