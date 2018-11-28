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

string C;
int k;

void solve() {
    cin >> C >> k;
    int changes = 0;
    for (int i = 0; i < C.length(); i++) {
        if (C[i] == '+') {
            continue;
        }
        bool canChange = (i + k <= C.length());
        if (!canChange) {
            printf("IMPOSSIBLE\n");
            return;
        }
        changes++;
        for (int j = i; j < i + k; j++) {
            C[j] = '+' + '-' - C[j];
        }
    }
    printf("%d\n", changes);
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
