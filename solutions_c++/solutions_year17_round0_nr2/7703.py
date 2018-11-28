//
//  TidyNumbers.cpp
//  GoogleCodeJam
//
//  Created by Carlos Rivera on 4/8/17.
//  Copyright © 2017 Carlos Rivera. All rights reserved.
//

#include "TidyNumbers.hpp"
#include <iostream> 
#include <string>

using namespace std;

int main() {
    
    int t;
    unsigned long long n;
    cin >> t;
    string input;
    string tidy;
    
    for (int i = 1; i <= t; ++i) {
        cin >> n;
        input = to_string(n);
        
        if (input.length() == 1) {
            tidy = input;
        } else {
            tidy = input;
            char prev;
            char curr;
            for (unsigned long i = input.length() - 1; i >= 1; i--) {
                prev = tidy[i];
                curr = tidy[i-1];
                if (curr > prev) {
                    tidy[i-1] = curr - 1;
                    for (unsigned long j = i; j < tidy.length(); j++) {
                        tidy[j] = '9';
                    }
                }
            }
            
        }
        
        if (tidy[0] == '0') {
            tidy.erase(0,1);
        }
        
        cout << "Case #" << i << ": " << tidy << endl;
    }
    return 0;
}