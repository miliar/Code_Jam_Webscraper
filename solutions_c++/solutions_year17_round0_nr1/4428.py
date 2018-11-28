#include <bits/stdc++.h>

using namespace std;

int solve(const string &s, int k) {
    string ts = s;
    int res = 0;
    for (int i = 0; i + k <= (int) s.size(); ++i) {
        if (ts[i] == '-') {
            ++res;
            for (int j = i; j < i + k; ++j) {
                if (ts[j] == '-')
                    ts[j] = '+';
                else
                    ts[j] = '-';
            }
        }
    }
    for (char c : ts) {
        if (c == '-')
            return -1;
    }
    return res;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        string s;
        int k;
        cin >> s >> k;
        cout << "Case #" << i << ": ";
        int res = solve(s, k);
        if (res < 0)
            cout << "IMPOSSIBLE";
        else
            cout << res;
        cout << "\n";
    }
}
