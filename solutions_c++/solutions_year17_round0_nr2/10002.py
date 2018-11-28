//
//  main.cpp
//  Problem-A
//
//  Created by Wenzhen Zhu on 4/8/17.
//  Copyright © 2017 Wenzhen Zhu. All rights reserved.
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

#define filename "B-small-attempt0"

using namespace std;

struct input {
    long N;
};

struct output {
    long N;
};

void read(ifstream &in, input &test) {
    in >> test.N;
}

void write(ofstream &out, output test) {
    out << test.N;
}

bool isTidyNumber(long num){
    string n = to_string(num);
    if(n.size() == 1){
        return true;
    } else{
        for(int i = 0; i < n.size() -1 ; i++){
            if(n[i] <= n[i+1]){
                continue;
            }else{
                return false;
            }
        }
        return true;
    }
    
}

output solve (input test) {
    output result;
    
    // Solution
    if (test.N == 0){
        result.N = 0;
    }
    
    for(long i = test.N; i >= 1; i--){
        if(isTidyNumber(i)){
            result.N = i;
            break;
        }
    }
    return result;
}

void readAll(vector <input> &tests) {
    ifstream in("/Users/wenzhen/Downloads/" + (string)filename + ".in");
    
    int T;
    in >> T;
    tests.resize(T);
    for (int i = 0; i < T; i++) {
        read(in, tests[i]);
    }
    in.close();
}

void solveAll(vector <input> &tests, vector <output> &results) {
    results.resize(tests.size());
    for (int i = 0; i < tests.size(); i++) {
        results[i] = solve(tests[i]);
    }
}

void writeAll(vector <output> &results) {
    ofstream out("/Users/wenzhen/Downloads/" + (string)filename + ".out");
    
    out << "Case #1: ";
    write(out, results[0]);
    for (int i = 1; i < results.size(); i++) {
        out << endl << "Case #" << i+1 << ": ";
        write(out, results[i]);
    }
    
    out.close();
}



int main(int argc, const char * argv[]) {
    vector <input> tests;
    vector <output> results;
    
    readAll(tests);
    solveAll(tests, results);
    writeAll(results);
    //cout << isTidyNumber(99) << endl;
    
    return 0;
}
