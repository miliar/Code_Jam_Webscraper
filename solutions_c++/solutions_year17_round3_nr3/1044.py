//
//  main.cpp
//  cont
//
//  Created by v on 30/04/17.
//  Copyright © 2017 Vladimir Berezkin. All rights reserved.
//
#include <algorithm>
#include <bitset>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <numeric>
#include <set>
#include <vector>
#include <math.h>
using namespace std;
//  !!!SMALL 1
void f() {
    int N, K;
    cin >> N >> K;
    double U;
    cin >> U;
    vector<double> P(N);
    for (int i = 0; i < N; ++i) {
        cin >> P[i];
    }
    sort(P.begin(), P.end());
    for (int i = 0; i < N && U > 0.0 && P[i] < 1.0; ++i) {
        if (i == N - 1 || P[i+1] > P[i]) {
            double next = i < N - 1 ? P[i+1] : 1.0;
            double need = next - P[i];
            double has = U / double(i+1);
            double add = min(need, has);
            for (int j = 0; j <= i; ++j) {
                P[j] += add;
                U -= add;
            }
        }
    }
    double res = accumulate(P.begin(), P.end(), 1.0, ^(double a, double b) {
        return a*b;
    });
    cout << fixed << setprecision(6) << res;
    cout << endl;
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
