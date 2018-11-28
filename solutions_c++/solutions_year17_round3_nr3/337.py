#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <thread>
using namespace std;

const double eps = 1e-8;
bool solve(const vector<double> &vec, double mid, double u) {
    for (double x : vec)
        u -= max(mid - x, 0.0);
    return u > 0;
}


int main() {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int casnum;
    cin >> casnum;
    for (int casid = 1; casid <= casnum; ++casid) {
        int n, k;
        double u;
        cin >> n >> k >> u;

        vector<double> vec(n);
        for (int i = 0; i < n; ++i)
            cin >> vec[i];

        double l = 0.0, r = 1.0;
        while (r - l > eps) {
            double mid = (l + r) / 2.0;
            if (solve(vec, mid, u)) l = mid;
            else r = mid;
        }

        double res = 1.0;
        for (double x : vec)
            res *= max(x, l);
        printf("Case #%d: %.7lf\n", casid, res);
    }
    return 0;
}

