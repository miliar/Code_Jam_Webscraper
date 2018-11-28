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
#include <numeric>
using namespace std;
const double pi = 3.1415926535897;
double get_a(double r) {return pi * r * r;}
double get_b(double r, double h) {return 2.0 * r * pi * h;}
double solve(const vector<pair<double, double>> &vec, int n, int k, int last) {
    vector<double> f;
    double res = 0;
    for (int i = 0; i < last - 1; ++i) {
        double r = vec[i].first, h = vec[i].second;
        f.push_back(get_b(r, h));
    }

    sort(f.begin(), f.end(), greater<double>());
    double r = vec[last-1].first, h = vec[last-1].second;
    double b = accumulate(f.begin(), f.begin() + k - 1, 0.0);
    double a = get_a(r);
    double c = get_b(r, h);
    return a + b + c;
}


int main() {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int casnum;
    cin >> casnum;
    for (int casid = 1; casid <= casnum; ++casid) {
        int n, k;
        cin >> n >> k;
        vector<pair<double, double>> vec;
        for (int i = 0; i < n; ++i) {
            double r, h;
            cin >> r >> h;
            vec.push_back(make_pair(r, h));
        }

        sort(vec.begin(), vec.end());

        double res = 0;
        for (int i = n; i >= k; --i) {
            double tmp = max(res, solve(vec, n, k, i));
            res = max(res, tmp);
        }
        printf("Case #%d: %.7lf\n", casid, res);
    }
    return 0;
}

