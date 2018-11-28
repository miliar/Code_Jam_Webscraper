//
//  main.cpp
//  OversizedPancakeFlipper
//
//  Created by Hjalmar Basile on 08/04/2017.
//  Copyright © 2017 Hjalmar Basile. All rights reserved.
//

#include <iostream>
#include <string>

using namespace std;

int main() {
    
    int t;
    cin >> t;
    
    for(int t_i = 1; t_i <= t; t_i++) {
        string s;
        int k;
        cin >> s >> k;
        
        int flips = 0;
        int i;
        long long loop_end_i = s.size() - k;
        for(i = 0; i <= loop_end_i; i++) {
            if(s[i] == '-') {
                // flip k pancakes starting from i
                int loop_end_j = i + k;
                for(int j = i; j < loop_end_j; j++) {
                    if(s[j] == '-') {
                        s[j] = '+';
                    } else{
                        s[j] = '-';
                    }
                }
                flips++;
            }
        }
        
        // check if there are remaining blank side pancakes
        bool good = true;
        while(i < s.size()) {
            if(s[i] == '-') {
                good = false;
                break;
            }
            i++;
        }
        
        cout << "Case #" << t_i << ": ";
        cout << (good ? to_string(flips) : "IMPOSSIBLE") << endl;
    }
    
    return 0;
}
