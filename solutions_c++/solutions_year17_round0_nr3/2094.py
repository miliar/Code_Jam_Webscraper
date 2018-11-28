#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

int solve() {
    map<long long, long long> spaces;
    long long n, k;
    cin >> n >> k;
    spaces[n] = 1;
    while(true) {
        long long mx = spaces.rbegin() -> first;
        cerr << mx << ' ';
        long long l = (mx - 1) / 2;
        long long r = mx - 1 - l;

        k -= spaces[mx];
        if (k <= 0) {
            cout << r << ' ' << l << endl;
            return 0;
        }

        spaces[l] += spaces[mx];
        spaces[r] += spaces[mx];
        spaces.erase(mx);
    }
}

int main()
{
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}
