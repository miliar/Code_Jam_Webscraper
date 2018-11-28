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
    freopen("/Users/kdutta/personal/work/contest/contest/in-C-2", "r", stdin);
    freopen("/Users/kdutta/personal/work/contest/contest/out-C-2", "w", stdout);
    
    int test, case_no = 0;
    int n, k;
    cin >> test;
    std::multiset<int, greater<int>> a;
    multiset<int,greater<int> >::iterator it;
    while( test-- ) {
        cout << "Case #"<< ++case_no <<": ";
        cin >> n >> k;
        int t = n;
        int  r1 = 0, r2 = 0;
        a.clear();
        while( k -- ) {
            r1 = t/2;
            r2 = r1;
            if( !(t % 2) ) r2--;
            a.insert(r1);
            a.insert(r2);
            it = a.begin();
            t = *it;
            a.erase(it);
        }
        cout << r1 << " " << r2 << endl;
        
	}
    return 0;
}
