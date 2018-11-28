//
//  2k17a.cpp
//  
//
//  Created by Vivek Nadimpalli on 4/7/17.
//
//

#include <stdio.h>
#include <iostream>
#include <fstream>
using namespace std;


int done(string s) {
    int n = s.length();
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '+') count++;
    }
    if (count == n) return 1;
    else return 0;
}


int main() {
    ifstream infile;
    infile.open("in1.txt");
    ofstream outfile;
    outfile.open("out1.txt");
    int t;
    infile >> t;
    int flag = 0;
    string s1;
    int k;
    for (int i = 1; i <= t; i++) {
        infile >> s1;
        infile >> k;
        int iter = 0;
        flag = 0;
        int pcount = 0, ncount = 0;
        for (int j = 0; j < s1.length(); j++) {
            if (s1[j] == '+') pcount++;
        }
        //already happy side up
        if (pcount == s1.length()) {
            outfile << "Case #" << i << ": " << 0 << endl;
            continue;
        }
        else { // not all are happy side up
            //scan the string until the first - is hit
            while (!done(s1)) {
                int j;
                for (j = 0; j < s1.length(); j++) {
                    if (s1[j] == '-')
                        break;
                }
                if (s1.length() - j < k) {
                    outfile << "Case #" << i << ": IMPOSSIBLE" << endl;
                    flag = 1;
                    break;
                }
                else {
                    iter++;
                    for (int l = j; l < j + k; l++) {
                        if (s1[l] == '+') s1[l] = '-';
                        else if (s1[l] == '-') s1[l] = '+';
                    }
                }
            }
            if (flag == 0)
                outfile << "Case #" << i << ": " << iter << endl;
        }
    }
    return 0;
}
