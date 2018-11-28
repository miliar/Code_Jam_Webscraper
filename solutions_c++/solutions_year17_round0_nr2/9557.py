//
//  main.cpp
//  test
//
//  Created by 陆洲 on 4/9/17.
//  Copyright © 2017 陆洲. All rights reserved.
//

#include <iostream>
#include <cstdlib>
#include <cstdio>
using namespace std;

string s;

void gao(){
    int n = s.size();
    for (int j=1;j<n;++j){
        if (s[j] < s[j-1]){
            
            int t = j-1;
            while (t && s[t-1] == s[t]) --t;
            if (t || s[t] != '1'){
                s[t] = s[t] - 1;
                for (int tt=t+1;tt<n;++tt) s[tt] = '9';
                return;
            }
            else{
                s.clear();
                for (int i=0;i<n-1;++i){
                    s += '9';
                }
                return;
            }
        }
    }

}

int main() {
    freopen("/Users/luzhou/Desktop/in.txt", "r", stdin);
    freopen("/Users/luzhou/Desktop/out.txt", "w", stdout);
    int T; cin >> T;
    for (int i=1;i<=T;++i){
        cin >> s;
        
        // 1223
        //
        
        gao();
        cout << "Case #" << i << ": " << s << endl;
    }
    
    return 0;
}
