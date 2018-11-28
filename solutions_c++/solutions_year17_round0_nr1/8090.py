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

int main(int argc, const char * argv[]) {

    freopen("/Users/kdutta/personal/work/contest/contest/in-A", "r", stdin);
    freopen("/Users/kdutta/personal/work/contest/contest/out-B", "w", stdout);
    
    int test, k, case_no = 0;
    string s;
    cin >> test;
    while( test-- ) {
        cout << "Case #"<< ++case_no <<": ";
        cin >> s >> k;
        int cnt = 0;
        for(int i=0; i<s.size(); i++ ) {
            if( s[i] == '-' && (i + k) <= s.size() ) {
                for( int j=i; j < (i+k); j++) {
                    s[j] = ( s[j] == '-' ) ? '+' : '-';
                }
                cnt++;
            }
        }
        int f = 1;
        for(int i=0; i<s.size(); i++ ) {
            if( s[i] == '-' ) {
                cout << "IMPOSSIBLE" << endl;
                f = 0;
                break;
            }
        }
        if( f ) cout << cnt << endl;
    }
    return 0;
}
