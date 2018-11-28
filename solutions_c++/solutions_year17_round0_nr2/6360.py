//
//  main.cpp
//  codejam
//
//  Created by Maksim Piriyev on 4/8/17.
//  Copyright © 2017 Maksim Piriyev. All rights reserved.
//

#include <iostream>
using namespace std;

int solve(char* s,int n){
    int last = 9;
    for (int i = n-1; i >= 0; i--) {
        if( s[i] > last){
            s[i]--;
            for (int j=i+1; j<n; j++) {
                s[j] = 9;
            }
        }
        last = s[i];
    }
    int i = 0;
    while(s[i] == 0 && i<n) i++;
    return i;

}

int main(int argc, const char * argv[]) {
    int N,K;
    cin>>N;
    string s;
    for (int n = 0; n<N; n++) {
        cin>>s;
        
        char* c = new char[s.length()+1];
        memcpy(c, s.c_str(), s.length());
        for (int j=0; j<s.length(); j++) {
            c[j] -= '0';
        }
        int r = solve(c,s.length());
        
        printf("Case #%d: ",(n+1));
        for(;r<s.length();r++){
            printf("%d",(int)c[r]);
        }
        printf("\n");
        fflush(stdout);
        delete[] c;
    }
    return 0;
}
