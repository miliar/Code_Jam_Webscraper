//
//  main.cpp
//  PancakeFlipper
//
//  Created by Guanyao Huang on 4/7/17.
//  Copyright © 2017 Guanyao Huang. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    int T, K;
    string S;
    cin >> T;
    for(int i=0; i<T; i++){
        cin>>S>>K;
        int retV = 0;
        for(int i=0; i<=S.length() - K; i++){
            if(S[i] == '-'){
                retV++;
                for(int j=i; j<i+K; j++){
                    if(S[j] == '-')
                        S[j] = '+';
                    else
                        S[j] = '-';
                }
            }
        }
        bool remain = false;
        for (int i = S.length()-K+1; i<(int)S.length(); i++){
            if(S[i] == '-'){
                remain = true;
                break;
            }
        }
        if(remain)
            cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << i+1 << ": "<< retV<< endl;
    }
    return 0;
}
