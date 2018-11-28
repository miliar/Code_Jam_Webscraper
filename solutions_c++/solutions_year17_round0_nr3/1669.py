#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdlib>

using namespace std;

#define TASKNAME ""

void solve(int test_number);

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.setf(ios::fixed);
    cout.precision(9);
    cerr.setf(ios::fixed);
    cerr.precision(3);
#ifdef LOCAL
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
#else
#endif
    int n = 1;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        solve(i);
    }
}

const int MAX_N = 100005; // TODO

typedef long long llong;

llong n, k;
pair<llong, llong> ans;
map<llong, llong > cnt;
priority_queue<llong> sizes;

void read_input() {
    cin >> n >> k;
}

void init() {
    // memset(a, -1, sizeof(a));
    while (!sizes.empty()) {
        sizes.pop();
    }
    cnt.clear();
}

void output(int test_number) {
    cout << "Case #" << test_number << ": ";
    if (ans.first < ans.second) {
        swap(ans.first, ans.second);
    }
    cout << ans.first << " " << ans.second << endl;
}

pair<llong, llong> get_minmax(llong n) {
    return make_pair((n + 1) / 2 - 1, n / 2);
}

void add_size(llong sz, llong c) {
    if (cnt.find(sz) == cnt.end()) {
        sizes.push(sz);
    }
    cnt[sz] += c;
}

void solve() {
    sizes.push(n);
    cnt[n] = 1;
    while (k) {
        llong x = sizes.top();
        sizes.pop();
        llong x_cnt = cnt[x];
        auto dists = get_minmax(x);
        if (x_cnt >= k) {
            ans = dists;
            break;
        }
        k -= x_cnt;
        add_size(dists.first, x_cnt);
        add_size(dists.second, x_cnt);
    }
}

void solve(int test_number) {
    read_input();
    init();
    solve();
    output(test_number);
}
