//
//  main.cpp
//  codejam
//
//  Created by Luis Giro on 14/7/17.
//  Copyright © 2017 Luis Giro. All rights reserved.
//

#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <math.h>
using namespace std;


bool B[2][1600];
bool C[2][1600][800];
int V[2][1600][800];
int dp(int p, int m, int mk, int ps) {
    
    //printf("%d",p);
    if (B[p][m] || mk < 0) {
        return 30000000;
    }
    if (m == 0 && ps != p) {
        return 30000000;
    }
    if (m == -1) {
        if (mk == 0) {
            return 0;
        }
        return 30000000;
    }
    if (m == -1 && mk == -1) return 1;
    if (m == -1) return 30000000;
    
    if(C[p][m][mk]) return V[p][m][mk];
    C[p][m][mk] = 1;
    return V[p][m][mk] = min(dp(p, m - 1, mk - 1, ps), dp(p ^ 1, m - 1, m - mk + 1, ps) + 1);
}

void clean() {
    for (int i = 0; i< 1600; i++) {
        for (int j = 0; j < 800; j++)
            C[1][i][j] = C[0][i][j] = V[1][i][j] = V[0][i][j] = 0;
    }
}


void solve() {
    int n1, n2, a, b;
    cin >> n1 >> n2;
    
    for (int i = 0; i< 1600; i++) {
        B[0][i] = B[1][i] = false;
        for (int j = 0; j < 800; j++)
            C[1][i][j] = C[0][i][j] = V[1][i][j] = V[0][i][j] = 0;
    }
    
    for(int i = 0; i < n1; i++) {
        cin >> a >> b;
        for (int j = a; j < b; j++)
            B[0][j] = true;
    }
    for(int i = 0; i < n2; i++) {
        cin >> a >> b;
        for (int j = a; j < b; j++)
            B[1][j] = true;
    }
    int r = 10000000;
    clean();
    r = min(r, dp(1, 1439, 720, 1));
    clean();
    r = min(r, dp(0, 1439, 720, 0));
    clean();
    r = min(r, dp(0, 1439, 720, 1) + 1);
    clean();
    r = min(r, dp(1, 1439, 720, 0) + 1);
    cout << r;
}

int main(int argc, const char * argv[]) {
    int testcases;
    cin >> testcases;
    
    for (int testcase = 1; testcase <= testcases; testcase++) {
        printf("Case #%d: ", testcase);
        solve();
        printf("\n");
    }
    return 0;
}
