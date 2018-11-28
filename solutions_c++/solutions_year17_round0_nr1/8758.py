//
//  main.cpp
//  codejam
//
//  Created by 김다빈 on 2017. 4. 8..
//  Copyright © 2017년 김다빈. All rights reserved.
//

#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <fstream>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
    int t, n, cnt, i, j;
    string s;
    ifstream fin("/Users/KimDaBin/Desktop/A-large1.in");
    ofstream fout("/Users/KimDaBin/Desktop/output1_r.txt");
    
    fin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int idx = 1; idx <= t; ++idx) {
        fin >> s;
        fin >> n;
        cnt = 0;
        for ( i = 0; i< s.length(); i++) {
            if (i <= s.length() - n ) {
                if (s[i] == '-') {
                    for (j = 0; j < n; j++) {
                        if(s[i+j] == '+') s[i+j] = '-';
                        else s[i+j] = '+';
                    }
                    cnt++;
                }
            } else {
                if (s[i] == '-') cnt = -1;
            }
        }
        if (cnt != -1)
            fout << "Case #" << idx << ": " << cnt << endl;
        else
            fout << "Case #" << idx << ": " << "IMPOSSIBLE" << endl;
    }
    return 0;
}
