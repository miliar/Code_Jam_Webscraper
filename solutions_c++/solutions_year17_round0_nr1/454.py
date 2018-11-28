//
//  main.cpp
//  CJ_QR1
//
//  Created by Yuto Murashita on 08/04/2017.
//  Copyright © 2017 Yuto Murashita. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;

class solve{
    int K;
public:
    int flip_N;
    string S;
    solve(string s, int k){
        S = s;
        K = k;
        flip_N=0;
    }
    void flip(int i, int K){
        for(int j=i; j<i+K; j++){
            if(S[j]=='+') S[j]='-';
            else S[j]='+';
        }
        flip_N++;
    }
    void prc(int K){
        for(int i=0; i<S.length()-K+1; i++){
            if(S[i]=='-') flip(i, K);
        }
    }
    bool all_h(void){
        for(int i=0; i<S.length(); i++){
            if(S[i]=='-') return false;
        }
        return true;
    }
};

int main(int argc, const char * argv[]) {
    int T, K;
    string S;
    cin >> T;
    for(int t=1; t<=T; t++){
        cin >> S >> K;
        solve tmp(S, K);
        tmp.prc(K);
        if(tmp.all_h()){
            cout << "Case #" << t << ": " << tmp.flip_N << endl;
        }
        else{
            cout << "Case #" << t << ": IMPOSSIBLE" <<  endl;
        }
    }
    
    return 0;
}
