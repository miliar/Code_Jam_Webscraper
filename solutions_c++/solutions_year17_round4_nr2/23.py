#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <iomanip>
#include <string>
#include <sstream>
#include <cmath>
#include <cassert>
#include <cstring>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

int n, c, m;
vector<pair<int, int>> tix;
vector<int> t2;
vector<int> c2;

bool feas(int rides) {
    if (rides < *max_element(c2.begin(), c2.end())) return false;
    int left = 0;
    for (int i = 0; i < n; ++i) {
        left += rides;
        if (t2[i] > left) return false;
        left -= t2[i];
    }
    return true;
}

int promos(int rides) {
    int pr = 0;
    for (int i = n; i--; ) {
        if (t2[i] > rides) pr += t2[i] - rides;
    }
    return pr;
}

int main() {
    int T;
    cin >> T;
    for (int caseno = 1; caseno <= T; ++caseno) {
        cin >> n >> c >> m;
        tix.resize(m);
        t2.assign(n, 0);
        c2.assign(c, 0);
        for (int i = 0; i < m; ++i) {
            cin >> tix[i].first >> tix[i].second;
        }
        for (auto&&t : tix) { t2[t.first-1]++; }
        for (auto&&t : tix) { c2[t.second-1]++; }
        int hi = 1;
        while (!feas(hi)) {
            hi = hi * 2;
        }
        int lo = hi / 2;
        while (hi > lo + 1) {
            int mid = (lo + hi) / 2;
            if (feas(mid)) {
                hi = mid;
            } else {
                lo = mid;
            }
        }

        printf("Case #%d: %d %d\n", caseno, hi, promos(hi));
    }
}
