//
//  main.cpp
//  CodeJam
//
//  Created by Gavriel Hirsch on 3/9/17.
//  Copyright © 2017 Gavriel Hirsch. All rights reserved.
//

#include <iostream>
#include <math.h>
using namespace std;

void pancake_output(){
    int cases, k;
    string s;
    cin >> cases;
    int flips, len;
    int solvable;
    for(int i = 0; i < cases; i++){
        cin >> s >> k;
        len = (int) s.length();
        solvable = 1;
        flips = 0;
        cout << "Case #" << i+1 << ": ";
        for(int j = 0; j < len - k + 1; j++){
            if(s[j] == '-'){
                flips++;
                for(int l = 1; l < k; l++){
                    if(s[j + l] == '-')
                        s[j + l] = '+';
                    else
                        s[j + l] = '-';
                }
            }
        }
        for(int j = len - k + 1; j < len; j++){
            if(s[j] == '-')
                solvable = 0;
        }
        if(solvable)
            cout << flips << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
}

int main(int argc, const char * argv[]) {
    pancake_output();
}
