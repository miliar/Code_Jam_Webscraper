//
//  main.cpp
//  B
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

#define filename "B-large"

using namespace std;

struct input {
    int64_t number;
};

struct output {
    int64_t number;
};

void read(ifstream &in, input &test) {
    in >> test.number;
}

void write(ofstream &out, output test) {
    out << test.number;
}

vector <int> toDigits (int64_t input) {
    vector<int> result;
    while (input > 0) {
        result.push_back(input % 10);
        input /= 10;
    }
    return result;
}

int64_t fromDigits (vector<int> digits) {
    int64_t result = 0;
    for (int i = (int)digits.size()-1; i >= 0; i--) {
        result *= 10;
        result += digits[i];
    }
    return result;
 }

output solve (input test) {
    output result;
    
    vector<int> digits = toDigits(test.number);
    
    for (int k = 0; k < digits.size() - 1; k++) {
        if (digits[k] < digits[k+1]) {
            for (int i = 0; i <= k; i++) {
                digits[i] = 9;
            }
            digits[k+1]--;
        }
    }
    
    result.number = fromDigits(digits);
    
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
