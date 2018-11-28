//
//  main.cpp
//  contest
//
//  Created by Atanu Dutta on 3/13/17.
//  Copyright © 2017. All rights reserved.
//

#include <stdio.h>
#include <memory.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <map>
#include <algorithm>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <string>
#include <iostream>
#include <stdio.h>

using namespace std;

#define max(a,b) ( a < b ? b : a )
#define min(a,b) ( a > b ? b : a )
#define alter(move) ( ( move + 1 ) % 2 )
#define inf -1234567890
#define MAX_SIZE 19
#define MOD 1000000007
#define T long long int
#define PI  3.14159265358979323846

vector< pair<T,T> > in;
T dp[1001][1001];
T n, k;

T memo( T pos, T k, T r, T area ) {
    
    if( k == 0 ) return area;
    
    if( dp[pos][k] != -1 ) return dp[pos][k];
    
    T res = -1;
    for(T i = pos; i <= n - k; i++ ) {
        T area1 = (in[i].first) * (in[i].first) - (r*r) + 2 * in[i].first * in[i].second;
        res = max( res, memo(i+1, k - 1, in[i].first, area + area1 ) );
    }
    
    return (dp[pos][k] = res);
}


int main(int argc, const char * argv[]) {
    freopen("/Users/kdutta/personal/work/contest/contest/A-small-attempt2.in", "r", stdin);
    freopen("/Users/kdutta/personal/work/contest/contest/A-small-attempt2.out", "w", stdout);
    
    int test, case_no = 0;
    cin >> test;
    T r, h;
    while( test-- ) {
        cout << "Case #"<< ++case_no <<": ";
        cin >> n >> k;
        in.clear();
        for(int i = 0; i<n; i++) {
            cin >> r >> h;
            in.push_back(make_pair(r, h));
        }
        sort(in.begin(), in.end());
        //memset(dp, -1, sizeof(T)*1001*1001);
        //double ans =  memo(0, k, 0, 0) * PI;
        double ans = 0;
        for(T i = 1; i < (1 << n); i++ ) {
            T j = i;
            int cnt = 0;
            int pos[25], index = 0;
            while( j ) {
                if( j & 1 ) {
                    pos[cnt++] = index;
                }
                j >>= 1;
                index++;
            }
            if( cnt == k ) {
                T r = 0;
                for(int j = 0; j < k; j++ ) {
                    r += (in[pos[j]].first*in[pos[j]].first) + 2*in[pos[j]].first*in[pos[j]].second;
                    if(j) r -= (in[pos[j-1]].first * in[pos[j-1]].first);
                }
                if( ans < r ) ans = r;
            }
        }
        printf("%.6lf\n", ans * PI);
	}
    return 0;
}
