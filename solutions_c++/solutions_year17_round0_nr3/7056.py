//
//  codejam pC.cpp
//  Sprout
//
//  Created by vistor on 09/04/2017.
//  Copyright © 2017 vistor. All rights reserved.
//

#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int t, Case = 1;
    cin >> t;
    while(t--){
        int n, m;
        cin >> n >> m;
        bool seq[n+2];
        memset(seq, 0, sizeof(seq));
        seq[0] = seq[n+1] = 1;
        int l = -1, r = -1, ans;
        for(int i = 1 ; i <= n ; i++){
            if(min(i-1, n-i) > l){
                l = min(i-1, n-i);
                r = max(i-1, n-i);
                ans = i;
            }
            else if(min(i-1, n-i) == l && max(i-1, n-i) > r){
                l = min(i-1, n-i);
                r = max(i-1, n-i);
                ans = i;
            }
        }
        while(m-- > 1){
            seq[ans] = 1;
            int l = -1, r = -1;
            for(int i = 1 ; i <= n ; i++){
                if(!seq[i]){
                    int L = i, R = i;
                    while(!seq[L - 1]) L--; L = i - L;
                    while(!seq[R + 1]) R++; R = R - i;
                    
                    if(min(L, R) > l){
                        l = min(L, R);
                        r = max(L, R);
                        ans = i;
                    }
                    else if(min(L, R) == l && max(L, R) > r){
                        l = min(L, R);
                        r = max(L, R);
                        ans = i;
                    }
                }
            }
        }
        
        int i, L, R;
        i = L = R = ans;
        while(!seq[L - 1]) L--; L = i - L;
        while(!seq[R + 1]) R++; R = R - i;
        
        cout << "Case #" << Case++ << ": " << max(L, R) << " " << min(L, R) << endl;
     }
}
