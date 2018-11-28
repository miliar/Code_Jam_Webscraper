//
//  main.cpp
//  CJ
//
//  Created by Brian Lui on 1/4/2017.
//  Copyright © 2017 Brian Lui. All rights reserved.
//

#include <iostream>
#include <string>

using namespace std;

int main(int argc, const char * argv[]) {
    int t;
    cin >> t;
    int caseN = 1;
    string s;
    int k;
    char arr[1000];
    
    while (t--) {
        cin >> s >> k;
        int len = s.length();
        
        for (int i = 0; i < len; i++) {
            arr[i] = (s[i] == '+') ? 0 : 1;
        }
        
        int count = 0;
        for (int j = 0; j <= len - k; j++) {
            if (arr[j] == 1) {
                for (int m = 0; m < k; m++) {
                    arr[j + m] = 1 - arr[j + m];
                }
                count++;
            }
        }
        
        int sum = 0;
        for (int l = 0; l < k; l++) {
            sum += arr[len - k + l];
        }
        
        if (sum > 0) {
            cout << "Case #" << caseN++ << ": " << "IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << caseN++ << ": " << count << endl;
        }
    }

    
    return 0;
}
