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

bool kFlip(string& S, int pos, int k){
    if (pos + k > S.length()) return false;
    for (int i=0;i<k;i++){
        if (S[pos+i]=='+') S[pos+i]='-';
        else S[pos+i]='+';
    }
    return true;
}

int main() {
    int T;
    cin >> T;
    for (int t=1; t<=T; t++){
        string S;
        cin >> S;
        int K;
        cin >> K;
        int kflips = 0;
        for (int pos=0;pos<S.length();pos++){
            if (S[pos]=='-'){
                if (kFlip(S, pos, K)) kflips++;
                else {
                    kflips = -1;
                    break;
                }
            }
        }
        
        cout << "Case #"<<t<<": ";
        
        if (kflips == -1){
            cout << "IMPOSSIBLE\n";
        }
        
        else cout << kflips << endl;
        
    }
}
