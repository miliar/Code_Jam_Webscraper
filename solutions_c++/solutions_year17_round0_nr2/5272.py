//
//  mainB.cpp
//  CJ
//
//  Created by Brian Lui on 7/4/2017.
//  Copyright © 2017 Brian Lui. All rights reserved.
//

#include <stdio.h>

#include <iostream>
#include <string>

using namespace std;

int main(int argc, const char * argv[]) {
    int t;
    cin >> t;
    int caseN = 1;
    unsigned long n, result;
    unsigned long curr;
    char arr[19];
    
    while (t--) {
        cin >> n;
        curr = n;
        
        for (int i = 0; i < 19; i++) {
            arr[i] = curr % 10;
            curr /= 10;
        }
        
        for (int i = 1; i < 19; i++) {
            if (arr[i] > arr[i - 1]) {
                arr[i]--;
                for (int j = 0 ; j < i; j++) {
                    if (arr[j] != 9) arr[j] = 9;
                }
            }
        }
        
        result = 0;
        for (int i = 18; i > 0; i--) {
            result += arr[i];
            result *= 10;
        }
        result += arr[0];
        
        cout << "Case #" << caseN++ << ": " << result << endl;
    }
    
    
    return 0;
}
