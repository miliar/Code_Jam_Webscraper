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

bool isTidy(int n) {
    
    while(n >= 10) {
        if((n%100)/10 > n%10) return false;
        n /= 10;
    }
    
    return true;
}

int main() {
    int t, n, cnt, i;
    ifstream fin("/Users/KimDaBin/Desktop/B-small-attempt0.in");
    ofstream fout("/Users/KimDaBin/Desktop/B-output0.txt");
    
    fin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int idx = 1; idx <= t; ++idx) {
        fin >> n;
        cnt = 0;
        for ( i = n; i >= 0; i--) {
            if(isTidy(i)) {
                cnt = i;
                break;
            }
        }
        
        fout << "Case #" << idx << ": " << cnt << endl;
    }
    return 0;
}
