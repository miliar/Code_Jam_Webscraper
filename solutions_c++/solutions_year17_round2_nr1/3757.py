//
//  mainE.cpp
//  CJ
//
//  Created by Brian Lui on 22/4/2017.
//  Copyright © 2017 Brian Lui. All rights reserved.
//

// Round 1B Quesiton 1

#include <stdio.h>
#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int main(int argc, const char * argv[]) {
    int t, d, n, k;
    double s;
    cin >> t;
    int caseN = 1;
    
    cout << fixed << setprecision(6);
    
    while (t--) {
        cin >> d >> n;
        double min = 0;
        double temp = 0;
        
        cin >> k >> s;
        temp = d * s / (d - k);
        min = temp;
        
        for (int i = 1; i < n; i++) {
            cin >> k >> s;
            temp = d * s / (d - k);
            if (temp < min) {
                min = temp;
            }
        }
        
        cout << "Case #" << caseN++ << ": " << min << endl;
    }
    
    
    return 0;
}
