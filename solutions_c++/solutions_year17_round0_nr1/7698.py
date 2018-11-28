//
//  PancakeFlipper.cpp
//  GoogleCodeJam
//
//  Created by Carlos Rivera on 4/8/17.
//  Copyright © 2017 Carlos Rivera. All rights reserved.
//

#include "PancakeFlipper.hpp"
#include <iostream>
#include <string>

using namespace std;

int main() {
    
    int t, k;
    int flips = 0;
    string s;
    cin >> t;
    
    for (int i = 1; i <= t; ++i) {
        cin >> s >> k;
        
        if (s.find('-') == string::npos) {
            // only + or -
            cout << "Case #" << i << ": " << 0 << endl;
        } else if (k > s.length()) {
            // spatula too big
            cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
        } else {
            
            for ( int j = 0 ; j < s.length(); j++) {
                if (s[j] == '-') {
                    
                    if ((j + k) < s.length()) {
                        // flip
                        for ( int l = j; l < (j+k); l++) {
                            if (s[l] == '-') {
                                s[l] = '+';
                            } else {
                                s[l] = '-';
                            }
                        }
                        flips++;
                        
                    } else if ((j + k) == s.length()) {
                        
                        int pos = j + 1;
                        bool passed = true;
                        while (pos < s.length()) {
                            if (s[pos] == '+') {
                                passed = false;
                            }
                            pos++;
                        }
                        
                        if (passed) {
                            flips++;
                            cout << "Case #" << i << ": " << flips << endl;
                            break;
                        } else {
                            cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
                            break;
                        }
                    }
                } else {
                    if ((j + k) == s.length()) {
                        int pos = j + 1;
                        bool passed = true;
                        while (pos < s.length()) {
                            if (s[pos] == '-') {
                                passed = false;
                            }
                            pos++;
                        }
                        
                        if (passed) {
                            cout << "Case #" << i << ": " << flips << endl;
                            break;
                        } else {
                            cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
                            break;
                        }
                        
                    }
                }
            }
        }
        flips = 0;
    }
    return 0;
}