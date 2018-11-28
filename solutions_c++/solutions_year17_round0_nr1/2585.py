#include <cstdio>
#include <iostream>
#include <string>

#define PROBLEM "A-large"

using namespace std;

int solve(string& s, int k) {
    int res = 0;
    int n = s.size();
    for (int i = 0; i + k <= n; ++i) {
        if (s[i] == '-') {
            ++res;
            for (int j = 0; j < k; ++j) {
                s[i + j] = '+' + '-' - s[i + j];
            }
        }
    }
    for (int i = n - k + 1; i < n; ++i) {
        if (s[i] == '-') {
            res = -1;
        }
    }
    return res;
}

int main()
{
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);

    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        string s;
        int k;
        cin >> s >> k;
        int res = solve(s, k);
        cout << "Case #" << t << ": ";
        if (res >= 0) {
            cout << res << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
