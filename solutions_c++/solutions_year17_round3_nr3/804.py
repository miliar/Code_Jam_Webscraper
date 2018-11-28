#include <algorithm>
#include <array>
#include <iostream>
#include <iomanip>
#include <math.h>
#include <queue>
#include <sstream>
#include <limits>
#include <list>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <set>
#include <vector>
#include <regex>

using namespace std;

const double PI = std::atan(1.0)*4;

double solve(vector<double> &p, double u) {
    double l = 0.0;
    double h = 1.0;
    double res = 0.0;

    for (int i = 0; i < 1000; ++i) {
        double mid = l + (h - l) / 2;
        double uu = 0.0;
        double prod = 1.0;
        for (double pi : p) {
            if (pi < mid) {
                uu += mid - pi;
                prod *= mid;
            } else {
                prod *= pi;
            }
        }
        if (uu <= u) {
            res = max(res, prod);
            l = mid;
        } else {
            h = mid;
        }
    }

    return res;
}


int main() {
    cin.sync_with_stdio(false);
    int T;
    cin >> T;
    cout.precision(10);
    cout << std::fixed;
    for (int t = 1; t <= T; ++t) {
        int n, k;
        cin >> n >> k;
        double u;
        cin >> u;
        vector<double> p(n);
        for (int i = 0; i < n; ++i) {
            cin >> p[i];
        }
        cout << "Case #" << t << ": " << solve(p, u) << endl;
    }

    return 0;
}
