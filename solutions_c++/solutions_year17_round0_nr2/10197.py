//
//  codejam pB.cpp
//  Sprout
//
//  Created by vistor on 09/04/2017.
//  Copyright © 2017 vistor. All rights reserved.
//

#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    long long int t, Case = 1; cin >> t;
    while(t--){
        long long int n; cin >> n;
        while(n > 0){
            string s = to_string(n);
            long long int imp = 0;
            for(long long int i = 1 ; i < s.size() ; i++) if(s[i] - s[i-1] < 0){ imp = 1; break; }
            if(imp) n--;
            else break;
        }
        cout <<"Case #" << Case++ << ": " << n << endl;
    }
    return 0;
}

