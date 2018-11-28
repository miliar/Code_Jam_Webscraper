//
//  1b-problem-a.cpp
//  googlecodejam2017
//
//  Created by Tony Li on 22/4/2017.
//  Copyright © 2017 ZeptoMind Creative Ltd. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <iomanip>

using namespace std;
typedef long long ll;
const int MAX_N = 1000;


int main(){
    int t,d_end, n;
    ll k, d;
    cin >> t;
    for (int i = 0; i<t; i++) {
        double res = 0;
        cin >> d_end >> n;
        double maxd = 0;
        for (int j =0 ; j< n; j++) {
            cin >> k >> d;
            maxd = max(maxd, (d_end-k)/(double)d);
        }
        res = d_end/maxd;
        cout << "Case #" << i+1 << ": " << setiosflags(ios::fixed) << setprecision(6)<< res <<endl;
    }
    
    return 0;
}
