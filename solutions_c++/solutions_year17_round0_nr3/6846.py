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
#include <vector>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
bool cmp(int f, int s) {
    return f>s;
}
int main() {
    int t, i, n, k, left =0 , right = 0;
    vector<int> buf;
    ifstream fin("/Users/KimDaBin/Desktop/C-small-1-attempt0.in");
    ofstream fout("/Users/KimDaBin/Desktop/C-output0.txt");

    fin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int idx = 1; idx <= t; ++idx) {
        fin >> n;
        fin >> k;
        buf.clear();
        left =(n-1)/2+(n-1)%2;
        right =(n-1)/2;
        
        buf.push_back(left);
        buf.push_back(right);

        for ( i = 0; i < k-1; i++) {
            left =(buf[0]-1)/2+(buf[0]-1)%2;
            right =(buf[0]-1)/2;
            
            buf.erase(buf.begin());
            buf.push_back(left);
            buf.push_back(right);
            
            sort(buf.begin(), buf.end(), cmp);
        }
        
        int max = (left > right) ? left : right;
        int min = (left <= right) ? left : right;
        fout << "Case #" << idx << ": " << max << " " << min << endl;
    }
    return 0;
}
