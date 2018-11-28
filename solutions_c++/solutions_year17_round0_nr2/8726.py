//
//  main.cpp
//  TidyNumbers
//
//  Created by Hjalmar Basile on 08/04/2017.
//  Copyright © 2017 Hjalmar Basile. All rights reserved.
//

#include <iostream>

using namespace std;

bool is_tidy(int n) {
    int d2 = n % 10;
    n /= 10;
    
    while(n > 0) {
        int d1 = n % 10;
        if(d1 > d2)
            return false;
        // else
        d2 = d1;
        n /= 10;
    }
    
    return true;
}

int main() {
    int t;
    cin >> t;
    
    for(int t_i = 1; t_i <= t; t_i++) {
        cout << "Case #" << t_i << ": ";
        
        int n;
        cin >> n;
        
        while(n >= 1) {
            if(is_tidy(n)) {
                cout << n << endl;
                break;
            }
            n--;
        }
    }
    
    return 0;
}
