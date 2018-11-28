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


struct Panc {
    
    double radius;
    double height;

}N[10005];

bool operator<(Panc a, Panc b) {
    if (a.radius != b.radius)
        return a.radius < b.radius;
    return a.height < b.height;
}

void solve() {
    
    int n, k;
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> N[i].radius >> N[i].height;
    }
    sort(N, N + n);
    double r = 0;
    
    priority_queue<double>Q;
    double s = 0;
    for (int i = 0; i < n; i++) {
        
        while (Q.size() >= k) {
            s += Q.top();
            Q.pop();
        }
        
        s += N[i].radius * N[i].height;
        Q.push(- N[i].radius * N[i].height);
        
        if (Q.size() == k) {
            r = max(r, 2 * s + N[i].radius * N[i].radius);
        }
        
        //cout << r << endl;
    }
    printf("%.9lf", r * M_PI);
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
