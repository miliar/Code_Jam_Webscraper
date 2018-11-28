//
//  main.cpp
//  Google Code Jam
//
//  Created by Angela Wu on 4/7/17.
//  Copyright © 2017 AngelaWu. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

/***************************************************************
 * Problem B: Tidy Numbers
 * 
 * tidy
 * Determines how many tidy numbers there are from 1 to N
 **************************************************************/
int tidy(int n) {
    int remainder = 0;
    int currNum = 0;

    for (int i = n; i > 0; i--) {
        currNum = i;
        remainder = i % 10;
        currNum /= 10;
        while (currNum != 0) {
            if (currNum % 10 <= remainder) {
                remainder = currNum % 10;
                currNum /= 10;
            }
            else
                break;
        }
        
        if (currNum == 0)
            return i;
    }
    
    return 1;
}

int main(int argc, const char * argv[]) {
    
    // Problem B: Tidy Numbers
    int input;
    cin >> input;
    int n; // range
    
    for (int i = 0; i < input; i++) {
        cin >> n;
        cout << "Case #" << i+1 << ": " << tidy(n) << endl;
    }
    
}
