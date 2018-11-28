//
//  main.cpp
//  codejam
//
//  Created by Luis Giro on 4/7/17.
//  Copyright © 2017 Luis Giro. All rights reserved.
//

#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

long long n;

long long lastTidy(long long x) {
    if (x < 10) {
        return x;
    }
    int lastD = x % 10;
    int last2D = (x % 100) / 10;
    long long tidy = 0;
    
    if (lastD >= last2D) {
        tidy = lastTidy(x / 10);
    } else {
        tidy = lastTidy(x / 10 - 1);
    }
    
    if (tidy * 10 + 9 < x) {
        return tidy * 10 + 9;
    }
    return tidy * 10 + lastD;
}

void solve() {
    cin >> n;
    cout << lastTidy(n) << endl;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int testcases;
    cin >> testcases;
    for (int testcase = 1; testcase <= testcases; testcase++) {
        printf("Case #%d: ", testcase);
        solve();
    }
    return 0;
}
