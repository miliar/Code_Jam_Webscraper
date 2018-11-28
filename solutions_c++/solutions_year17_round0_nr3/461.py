//
//  main.cpp
//  GCJ_QR_C
//
//  Created by Yuto Murashita on 08/04/2017.
//  Copyright © 2017 Yuto Murashita. All rights reserved.
//

#include <iostream>
using namespace std;

class part{
    long long K, L, NL, NS;
public:
    part(long long n, long long k){
        K = k;
        L = n;
        NL = 1; NS = 0;
    }
    void full_part(void){
        if(L%2==0){
            L/=2;
            NS=2*NS+NL;
        }else{
            L/=2;
            NL=2*NL+NS;
        }
    }
    long long length(void){
        long long N_part = 1;
        while(K>N_part){
            full_part();
            K-=N_part;
            N_part*=2;
        }
        if(K<=NL) return L;
        else return L-1;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    int T;
    long long N;
    long long K;
    cin >> T;
    for(int t=1; t<=T; t++){
        cin >> N >> K;
        part tmp(N, K);
        long long L = tmp.length();
        cout << "Case #" << t << ": " << L/2 << " " << L-L/2-1 << endl;
    }
    return 0;
}
