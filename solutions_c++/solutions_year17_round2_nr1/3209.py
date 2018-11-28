//
//  A.cpp
//  
//
//  Created by John Nevard on 4/22/17.
//
//

#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using std::cin;
using std::cout;
using std::cerr;
using std::vector;
using std::swap;

typedef vector<double> VD;

int main() {
    int n_cases;
    cin >> n_cases;
    for (int i = 1; i <= n_cases; ++i) {
        int d, n;
        cin >> d >> n;
        VD x(n), v(n);
        double v0 = 1E100;
        for (int j = 0; j < n; ++j) {
            cin >> x[j] >> v[j];
            if (v0 <= v[j]) continue;
            double t = x[j] / (v0 - v[j]);
            if (x[j] == d || v0 * t >= d) continue;
            v0 = d * v[j] / (d - x[j]);
        }
        printf("Case #%d: %.6lf\n", i, v0);
    }
    return 0;
}

