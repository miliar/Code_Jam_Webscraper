//
//  main.cpp
//  A. Oversized Pancake Flippe
//
//  Created by Jason Naldi on 08.04.17.
//  Copyright © 2017 jasonnaldi. All rights reserved.
//

#include <fstream>
#include <iostream>
#include <iomanip>

#define READ_IN in
#define PRINT_OUT out

using namespace std;

string path = "/Users/jason/Documents/School/Uni/CS/Bachelor/2nd semester/Computer Challenges Lab/Google Codejam/2017/";
string subpath = "1. Qualification Round/A. Oversized Pancake Flippe/Tests/";
string file_name = path + subpath + "small";
string file_in = file_name + "_input.txt";
string file_out = file_name + "_output.txt";

string s = "";
int k = 0;

void flip(ssize_t idx) {
    for (ssize_t i = idx; i < idx + k; ++i)
        s[i] = (s[i] == '+' ? '-' : '+');
}

void unflip(ssize_t idx) {
    flip(idx);
}

bool allFlippedRight() {
    for (char c : s)
        if (c == '-')
            return false;
    
    return true;
}

ssize_t getSmallestFlipsCount(ssize_t i = 0) {
    if (allFlippedRight())
        return 0;
    
    ssize_t smallestFlipsCount = -1;
    
    for (; i < s.size() - k + 1; ++i) {
        flip(i);
        
        ssize_t currentFlips = getSmallestFlipsCount(i+1); //+1 for next flip
        
        if (currentFlips >= 0 && (smallestFlipsCount < 0 || currentFlips < smallestFlipsCount))
            smallestFlipsCount = currentFlips + 1; // + 1 for current flip
    
        unflip(i);
    }
    
    return smallestFlipsCount;
}

int main(int argc, const char * argv[]) {
    // Speeds up input reading and output printing.
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    ifstream in(file_in);
    ofstream out(file_out);
    
    int tests = 0;
    READ_IN >> tests;
    
    for (int test = 1; test <= tests; ++test) {
        READ_IN >> s;
        READ_IN >> k;
        
        ssize_t flips = getSmallestFlipsCount();
        
        PRINT_OUT << "Case #" << test << ": " << (flips < 0 ? "IMPOSSIBLE" : to_string(flips)) << "\n";
    }
    
    return 0;
}
