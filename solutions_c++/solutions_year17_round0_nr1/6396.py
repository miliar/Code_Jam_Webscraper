//
//  main.cpp
//  codejam
//
//  Created by Maksim Piriyev on 4/8/17.
//  Copyright © 2017 Maksim Piriyev. All rights reserved.
//

#include <iostream>
using namespace std;

int solve(char* s,int n,int k){
    int rtn = 0;
    for (int i = 0; i < n; i++) {
        if( s[i] == '-'){
            if(i > n-k) return -1;
            for (int j=0; j<k; j++) {
                s[i+j] = s[i+j] == '-' ? '+' : '-';
            }
            rtn++;
        }
    }
    return rtn;

}

int main(int argc, const char * argv[]) {
    int N,K;
    cin>>N;
    string s;
    for (int n = 0; n<N; n++) {
        cin>>s>>K;
        
        char* c = new char[s.length()+1];
        memcpy(c, s.c_str(), s.length());
        int r = solve(c,s.length(),K);
        delete[] c;
        printf("Case #%d: %s\n",(n+1),r == -1 ? "IMPOSSIBLE": to_string(r).c_str());
    }
    return 0;
}
