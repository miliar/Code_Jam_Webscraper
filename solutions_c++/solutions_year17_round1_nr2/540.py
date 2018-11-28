//
//  main.cpp
//  B
//
//  Created by Max Piskunov on 4/14/17.
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
    vector<int> requirements;
    vector<vector<int> > packages; //packages[ingridient][package]
};

struct output {
    int kitCount;
};

void read(ifstream &in, input &test) {
    int N, P;
    in >> N >> P;
    test.requirements.resize(N);
    test.packages.resize(N);
    for (int i = 0; i < N; i++) test.packages[i].resize(P);
    
    for (int i = 0; i < N; i++) in >> test.requirements[i];
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < P; j++) {
            in >> test.packages[i][j];
        }
    }
}

void write(ofstream &out, output test) {
    out << test.kitCount;
}

int divideUp(int x, int y) {
    return (x + y - 1) / y;
}

bool match(pair<int, int> one, pair<int, int> two) {
    int left = max(one.first, two.first);
    int right = min(one.second, two.second);
    return right >= left;
}

output solve (input test) {
    output result;
    
    vector<vector<pair<int, int> > > ranges(test.packages.size(), vector<pair<int, int> >(test.packages[0].size()));
    for (int i = 0; i < test.packages.size(); i++) {
        for (int j = 0; j < test.packages[i].size(); j++) {
            ranges[i][j].first = divideUp(test.packages[i][j] * 10, 11 * test.requirements[i]);
            if (ranges[i][j].first == 0) ranges[i][j].first++;
            ranges[i][j].second = test.packages[i][j] * 10 / (9 * test.requirements[i]);
        }
    }
    
    for (int i = 0; i < test.packages.size(); i++) {
        sort(ranges[i].begin(), ranges[i].end());
    }
    
    /*for (int i = 0; i < test.packages.size(); i++) {
        for (int j = 0; j < test.packages[i].size(); j++) {
            cout << "(" << ranges[i][j].first << ", " << ranges[i][j].second << ")" << " ";
        }
        cout << endl;
    }
    cout << endl;*/

    vector<int> pointers(test.packages.size(), 0);
    result.kitCount = 0;
    
    while(true) {
        pair<int, int> commonRange(INT_MIN, INT_MAX);
        for (int i = 0; i < pointers.size(); i++) {
            commonRange.first = max(commonRange.first, ranges[i][pointers[i]].first);
            commonRange.second = min(commonRange.second, ranges[i][pointers[i]].second);
        }
        if (commonRange.second >= commonRange.first) {
            result.kitCount++;
            for (int i = 0; i < pointers.size(); i++) {
                pointers[i]++;
                if (pointers[i] == ranges[0].size()) return result;
            }
        } else {
            pair<int, int> smallest = make_pair(INT_MAX, INT_MAX);
            int smallestIndex = -1;
            for (int i = 0; i < pointers.size(); i++) {
                if (smallest > ranges[i][pointers[i]]) {
                    smallestIndex = i;
                    smallest = ranges[i][pointers[i]];
                }
            }
            pointers[smallestIndex]++;
            if (pointers[smallestIndex] == ranges[0].size()) return result;
        }
    }
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
