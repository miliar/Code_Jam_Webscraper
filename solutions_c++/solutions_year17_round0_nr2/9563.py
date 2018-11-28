//
//  2k17b.cpp
//  
//
//  Created by Vivek Nadimpalli on 4/7/17.
//
//

#include <stdio.h>
#include <iostream>
#include <fstream>

using namespace std;

int check(int num) {
    // check if number is tidy
    // if not then reduce the value until tidy
    
    int i = num;
    int count = num;
    int m = i % 10;
    i /= 10;
    while (i > 0) {
        int r = i % 10;
        if (m < r) {
            i = --count;
            m = i % 10;
            i /= 10;
            continue;
        }
        m = r;
        i = i / 10;
    }
    return count;
}

int main() {
    ifstream infile;
    ofstream outfile;
    infile.open("in1.txt");
    outfile.open("out1.txt");
    int t;
    infile >> t;
    int num;
    for (int i = 0; i < t; i++) {
        infile >> num;
        outfile << "Case #" << i+1 << ": " << check(num) << endl;
    }
    return 0;
}
