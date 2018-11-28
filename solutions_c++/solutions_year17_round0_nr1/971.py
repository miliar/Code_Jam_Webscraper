#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e5;

int n, p, a[maxn];
string pancakes;

void solve() {
    cin >> pancakes >> p;
    n = pancakes.size();
    for (int i = 0; i < n; i++) {
        a[i] = (pancakes[i] == '+');
    }

    int res = 0;
    for (int i = 0; i + p <= n; i++) {
        if (!a[i]) {
            ++res;
            for (int j = 0; j < p; j++) {
                a[i + j] = !a[i + j];
            }
        }
    }

    for (int i = 0; i < n; i++) {
        if (!a[i]) {
            cout << "IMPOSSIBLE";
            return;
        }
    }
    cout << res;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int numCases;
    cin >> numCases;
    for (int i = 1; i <= numCases; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
        cerr << i << endl;
    }
    return 0;
}
