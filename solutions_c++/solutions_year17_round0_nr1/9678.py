//
//  main.cpp
//  CodeJam
//
//  Created by Renfrew CHEN on 2017-04-08.
//  Copyright © 2017 Renfrew CHEN. All rights reserved.
//

#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::string;
using std::endl;

int main(int argc, const char * argv[]) {
    int numTests;
    
    cin >> numTests;
    
    for (int k = 0; k < numTests; ++k) {
        string pancakes;
        unsigned long K;
        
        cin >> pancakes >> K;
        int times = 0;
        
        char * cstr = new char [pancakes.length()+1];
        std::strcpy (cstr, pancakes.c_str());
        
        for (unsigned long i = 0; i <= pancakes.length() - K; ++i) {
            if (cstr[i] == '-') {
                ++times;
                for (int j = 0; j < K; ++j) {
                    if (cstr[i + j] == '-') {
                        cstr[i + j] = '+';
                    } else {
                        cstr[i + j] = '-';
                    }
                }
            }
        }
        
        bool isSolution = true;
        for (unsigned long i = pancakes.length() - K; i < pancakes.length(); ++i) {
            if (cstr[i] == '-') {
                isSolution = false;
                break;
            }
        }
        
        if (isSolution) {
            cout << "Case #" << k + 1 << ": " << times << endl;
        } else {
            cout << "Case #" << k + 1 << ": IMPOSSIBLE" << endl;
        }
    }
    
    return 0;
}
