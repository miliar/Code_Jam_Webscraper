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

const int MAX_N = 1005; // TODO

int d, n;
int x[MAX_N], v[MAX_N];

void read_input() {
    cin >> d >> n;
    for (int i = 0; i < n; i++) {
        cin >> x[i] >> v[i];
    }
}

void init() {
    // memset(a, -1, sizeof(a));
}

void output(int test_number) {
    cout << "Case #" << test_number << ": ";
}

void solve(int test_number) {
    read_input();
    init();

    double mx = 0;
    for (int i = 0; i < n; i++) {
        mx = max(mx, (double)(d - x[i]) / v[i]);
    }
    output(test_number);
    cout << d / mx << endl;
}
