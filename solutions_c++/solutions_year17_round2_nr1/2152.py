//
//  main.cpp
//  cont
//
//  Created by v on 22/04/17.
//  Copyright © 2017 Vladimir Berezkin. All rights reserved.
//
#include <algorithm>
#include <bitset>
#include <iomanip>
#include <iostream>
#include <set>
#include <vector>
using namespace std;

void f() {
    double D;
    int N;
    cin >> D >> N;
    using KS = pair<double, double>;
    vector<KS> ks(N);
    for (int i = 0; i < N; ++i) {
        cin >> ks[i].first >> ks[i].second;
    }
    double res = 0;
    for (int i = 0; i < N; ++i) {
        double t = (D - ks[i].first) / ks[i].second;
        if (t > res) {
            res = t;
        }
    }
    res = D / res;
    cout << fixed << setprecision(6) << res << endl;
}

int main() {
    int cases;
    cin >> cases;
    for (int cas = 1; cas <= cases; ++cas) {
        cout << "Case #" << cas << ": ";
        f();
    }
    return 0;
}
