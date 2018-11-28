//
//  main.cpp
//  Codejam2017
//
//  Created by Lavi on 2017-04-08.
//  Copyright © 2017 Lavi. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;


int main() {
    int T;
    cin >> T;
    for (int t=1; t<=T; t++){
        string S;
        cin >> S;
        for (int p=0;p<S.length()-1;p++){
            if (S[p+1]<S[p]){
                for (int k=p+1;k<S.length();k++) S[k]='9';
                S[p] -= 1;
                while (p > 0 && S[p-1] > S[p]){
                    S[p] = '9';
                    p--;
                    S[p] -= 1;
                }
                break;
            }
        }
        
        cout << "Case #"<<t<<": ";
        int p = 0;
        while (S[p]=='0') p++;
        while (p<S.length()){
            cout << S[p];
            p++;
        }
        cout << endl;
    }
}
