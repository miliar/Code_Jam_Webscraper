//
//  main.cpp
//  A
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

#define filename "A-large"

using namespace std;

struct input {
    vector<string> cake;
};

struct output {
    vector<string> cake;
};

void read(ifstream &in, input &test) {
    int R, C;
    in >> R >> C;
    test.cake.resize(R);
    for (int i = 0; i < R; i++) {
        in >> test.cake[i];
    }
}

void write(ofstream &out, output test) {
    for (int i = 0; i < test.cake.size(); i++) {
        out << endl;
        out << test.cake[i];
    }
}

output solve (input test) {
    output result;
    
    result.cake.resize(test.cake.size());
    for (int i = 0; i < test.cake.size(); i++) {
        result.cake[i].resize(test.cake[i].size(), '?');
    }
    
    for (int i = 0; i < test.cake.size(); i++) {
        for (int j = 0; j < test.cake[i].size(); j++) {
            result.cake[i][j] = test.cake[i][j];
        }
    }
    
    for (int i = 0; i < test.cake.size(); i++) {
        for (int j = 1; j < test.cake[i].size(); j++) {
            if (result.cake[i][j] == '?') result.cake[i][j] = result.cake[i][j-1];
        }
    }
    
    for (int i = 0; i < test.cake.size(); i++) {
        for (int j = (int)test.cake[i].length() - 2; j >= 0; j--) {
            if (result.cake[i][j] == '?') result.cake[i][j] = result.cake[i][j+1];
        }
    }
    
    for (int i = 1; i < test.cake.size(); i++) {
        if (result.cake[i][0] == '?') {
            for (int j = 0; j < test.cake[i].size(); j++) {
                result.cake[i][j] = result.cake[i-1][j];
            }
        }
    }
    
    for (int i = (int)test.cake.size() - 2; i >= 0; i--) {
        if (result.cake[i][0] == '?') {
            for (int j = 0; j < test.cake[i].size(); j++) {
                result.cake[i][j] = result.cake[i+1][j];
            }
        }
    }
    
    /*for (int i = 0; i < test.cake.size(); i++) {
        for (int j = 0; j < test.cake[i].size(); j++) {
            if (test.cake[i][j] != '?') {
                result.cake[i][j] = test.cake[i][j];
            } else if (j > 0) {
                result.cake[i][j] = result.cake[i][j-1];
            } else {
                for (int k = j + 1; k < test.cake[i].size(); k++) {
                    if (test.cake[i][k] != '?') result.cake[i][j] = test.cake[i][k];
                }
            }
            if (result.cake[i][j] != )
        }
    }*/
    
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
