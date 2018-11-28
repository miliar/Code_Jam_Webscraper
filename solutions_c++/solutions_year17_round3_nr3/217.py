#include <algorithm>
#include <iostream>
#include <cmath>
#include <vector>
#include <map>
using namespace std;


int readRational() {
    double x;
    cin >> x;
    return int(x * 10000 + 0.01);
}


double calcMaxProbability(const vector<int>& ps, int u, int k) {
    const int C = 10000;
    vector<int> cnt(C + 1);
    for (int p : ps) ++cnt[p];
    for (int c = 0; c < C; ++c) {
        if (cnt[c] > u) break;
        if (cnt[c]) {
            u -= cnt[c];
            cnt[c + 1] += cnt[c];
            cnt[c] = 0;
        }
    }
    vector<double> pps;
    for (int c = 0; c < C; ++c) {
        if (cnt[c] == 0) continue;
        double add = 0;
        if (u > 0) {
            add = u * 1.0 / cnt[c];
            u = 0;
        }
        while (cnt[c] > 0) {
            pps.push_back(c * 1.0 / C + add / C);
            --cnt[c];
        }
    }
    double res = 1;
    for (double p : pps) res *= p;
    return res;
}


int main() {
    ios_base::sync_with_stdio(false);
    int numTests;
    cin >> numTests;
    cout.precision(10);
    cout << fixed;
    for (int tId = 0; tId < numTests; ++tId) {
        int n, k;
        cin >> n >> k;
        int u = readRational();
        vector<int> p(n);
        for (int i = 0; i < n; ++i) p[i] = readRational();
        cout << "Case #" << tId + 1 << ": " << calcMaxProbability(p, u, k) << endl;
    }
    return 0;
}
