//
//  main.cpp
//  codejam
//
//  Created by Luis Giro on 4/7/17.
//  Copyright © 2017 Luis Giro. All rights reserved.
//

#include <cstdio>
#include <iostream>
#include <map>
#include <queue>

using namespace std;

long long n, k;

long long solution() {
    cin >> n >> k;
    map<long long, int> Counter;
    priority_queue<long long>queue;
    queue.push(n);
    Counter[n] = 1;
    while (queue.size() > 0) {
        long long x = queue.top();queue.pop();
        int c = Counter[x];
        k -= c;
        if (k <= 0) {
            return x;
        }
        long long xl = x / 2;
        long long xr = x - xl - 1;
        
        if (Counter[xl] == 0) {
            queue.push(xl);
        }
        Counter[xl] += c;
        
        if (Counter[xr] == 0) {
            queue.push(xr);
        }
        Counter[xr] += c;
    }
    return 0;
}

void solve() {
    long long s = solution() - 1;
    long long sr = s / 2;
    cout << s - sr << " " << sr << endl;
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
