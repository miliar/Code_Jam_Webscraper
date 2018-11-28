//
//  main.cpp
//  contest
//
//  Created by Atanu Dutta on 3/13/17.
//  Copyright © 2017. All rights reserved.
//
#include <map>
#include <algorithm>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <string>
#include <iostream>
#include <cstdio>
#include <stdio.h>
#include <memory.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

using namespace std;

#define max(a,b) ( a < b ? b : a )
#define min(a,b) ( a > b ? b : a )
#define alter(move) ( ( move + 1 ) % 2 )
#define inf -1234567890
#define MAX_SIZE 19
#define MOD 1000000007
#define T long long int

int main(int argc, const char * argv[]) {

    freopen("/Users/kdutta/personal/work/contest/contest/in-B", "r", stdin);
    freopen("/Users/kdutta/personal/work/contest/contest/out-B", "w", stdout);
    
    int test, case_no = 0;
    cin >> test;
    while( test-- ) {
        cout << "Case #"<< ++case_no <<": ";
        int n;
        cin >> n;
        while ( n ) {
            char s[10];
            sprintf(s, "%d", n);
            int done = 1;
            for(int i=0; i < strlen(s) - 1 ; i++) {
                if( s[i] > s[i+1]) {
                    done = 0;
                    break;
                }
            }
            if( done ) {
                cout << n << endl;
                break;
            }
            n--;
        }
	}
    
    return 0;
}
