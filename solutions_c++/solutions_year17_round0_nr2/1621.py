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

string n;
string ans;

void read_input() {
    cin >>  n;
}

void init() {
    // memset(a, -1, sizeof(a));
}

void output(int test_number) {
    cout << "Case #" << test_number << ": ";
    cout << ans << endl;
}

void solve() {
    bool f = false;
    for (int i = n.size() - 1; i >= 0; i--) {
        ans = n;
        if ((i == 0 && n[i] == '1') || n[i] == '0') {
            continue;
        }
        ans[i] = ans[i] - 1;
        for (int j = i + 1; j < n.size(); j++) {
            ans[j] = '9';
        }
        f = true;
        for (int j = 0; j < ans.size() - 1; j++) {
            if (ans[j] > ans[j + 1]) {
                f = false;
                break;
            }
        }
        if (f) {
            break;
        }
    }
    if (!f) {
        ans = string(n.size() - 1, '9');
    }
}

void solve(int test_number) {
    read_input();
    init();
    ans = n;
    for (int i = 0; i < n.size() - 1; i++) {
        if (n[i] > n[i + 1]) {
            solve();
            break;
        }
    }
    output(test_number);
}
