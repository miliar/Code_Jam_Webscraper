//
//  a.cpp
//  
//
//  Created by Lucca Siaudzionis on 2017-05-13.
//
//

#include <map>
#include <set>
#include <tuple>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int t, n, p;
int g[105];
int r[5];
int dp[4][105][105][105];

int solve(int cr, int r1, int r2, int r3){
    
    if(dp[cr][r1][r2][r3] != -1) return dp[cr][r1][r2][r3];
    
    if((r1 + r2 + r3) == 0) return 0;

    int c = 0;
    if(!cr) c++;

    int b = 0;
    if(r1) b = max(b, c + solve( (cr+1)%p, r1-1, r2, r3 ));
    if(r2) b = max(b, c + solve( (cr+2)%p, r1, r2-1, r3 ));
    if(r3) b = max(b, c + solve( (cr+3)%p, r1, r2, r3-1 ));

    return dp[cr][r1][r2][r3] = b;
}

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> t;

    for(int nc = 1;nc <= t;nc++){

        cin >> n >> p;
        for(int i = 0;i < 5;i++) r[i] = 0;
        for(int i = 1;i <= n;i++){
            cin >> g[i];
            r[g[i]%p]++;
        }

        cout << "Case #" << nc << ": ";

        if(p == 2){
            cout << (r[0] + (r[1]+1)/2) << endl;
        }
        /*else if(p == 3){
            int m = min(r[1], r[2]);
            int m2 = max(r[1], r[2]) - min(r[1], r[2]);
            m2 = (m2+2)/3;
            cout << (r[0] + m + m2) << endl;
        }*/
        else{
            memset(dp, -1, sizeof dp);
            cout << (r[0] + solve(0, r[1], r[2], r[3])) << endl;
        }
    }
    
    return 0;
}
