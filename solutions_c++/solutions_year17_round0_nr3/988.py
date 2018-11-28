#include <bits/stdc++.h>
using namespace std;

pair<long long, long long> f(long long n, long long k) {
    long long lsz = (n - 1) / 2;
    long long rsz = n - 1 - lsz;

    if (k == 1) {
        return {rsz, lsz};
    }
    --k;

    if (k % 2 == 1) {
        return f(rsz, k / 2 + 1);
    } else {
        return f(lsz, k / 2);
    }
}

void solve() {
    long long n, k;
    cin >> n >> k;
    auto res = f(n, k);
    cout << res.first << ' ' << res.second;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int numCases;
    cin >> numCases;
    for (int i = 1; i <= numCases; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << '\n';
        cerr << i << endl;
    }
    return 0;
}
