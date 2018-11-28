#include <iostream>
#include <algorithm>
#include <bitset>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <iomanip>
#include <queue>
#include <utility>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<int, char> pci;

bool IsIntersect(const pii& lhs, const pii& rhs) {
    int l = max(lhs.first, rhs.first);
    int r = min(lhs.second, rhs.second);
    return l <= r;
}

void Solve(int test_index) {
    int n, p;
    cin >> n >> p;
    vector<int> a(n);
    for (int& x : a) { cin >> x; }
    vector<vector<int>> b(n, vector<int>(p));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < p; ++j) {
            cin >> b[i][j];
        }
    }
    vector<vector<pii>> segs(n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < p; ++j) {
            // int lhs = (9 * b[i][j] + 10 * a[i] - 1) / (10 * a[i]);
            // int rhs = (11 * b[i][j]) / (10 * a[i]);
            int rhs = (10 * b[i][j]) / (9 * a[i]);
            int lhs = (10 * b[i][j] + 11 * a[i] - 1) / (11 * a[i]);
            // cerr << "i = " << i << endl;
            // cerr << "lhs = " << lhs << '\n';
            // cerr << "rhs = " << rhs << '\n';
            if (lhs > rhs) { continue; }
            segs[i].emplace_back(lhs, rhs);
        }
        sort(segs[i].begin(), segs[i].end());
    }
    int cnt = 0;
    vector<int> inds(n);
    for (const auto& seg : segs[0]) {
        bool flag = true;
        for (int i = 1; i < n; ++i) {
            while (inds[i] + 1 < segs[i].size() && segs[i][inds[i]].second < seg.first) { ++inds[i]; }
            if (inds[i] >= segs[i].size() || !IsIntersect(segs[i][inds[i]], seg)) {
                flag = false;
            }
        }
        if (flag) {
            ++cnt;
            for (int i = 1; i < n; ++i) { ++inds[i]; }
        }
    }
    cout << "Case #" << test_index + 1 << ": " << cnt << "\n";
}

int main() {
    std::ios_base::sync_with_stdio(false);
    int tests_count;
    cin >> tests_count;
    for (int test_index = 0; test_index < tests_count; ++test_index) {
        Solve(test_index);
    }
    return 0;
}
