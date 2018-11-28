//#include "testlib.h"
//#include <spoj.h>

#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>
#include <assert.h>
#include <time.h>
#include <memory.h>
#include <set>
#include <numeric>
#include <map>
#include <queue>
#include <stack>
#include <bitset>
#include <unordered_map>

using namespace std;

int d, n;
int x[1111], sp[1111];

bool inters(double sp1, int x2, double sp2) {
    if (sp1 < sp2) return false;
    return d * (sp1 - sp2) + 1e-8 > sp1 * x2;
}

bool ok(double my_speed) {
    for (int i = 0; i < n; ++i) {
        if (inters(my_speed, x[i], sp[i]))
            return false;
    }
    return true;
}

int main() {
    srand(31415);
   freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> d >> n;
        for (int i = 0; i < n; ++i) {
            cin >> x[i] >> sp[i];
        }
        
        double l = 0, r = 1e18;
        for (int i = 0; i < 500; ++i) {
            double m = (l + r) / 2;
            if (ok(m))
                l = m;
            else
                r = m;
        }
        cout << "Case #" << t << ": ";
        cout.precision(6);
        cout << fixed << l << "\n";
    }
    return 0;
}
