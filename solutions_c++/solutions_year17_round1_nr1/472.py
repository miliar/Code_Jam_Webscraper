#include <bits/stdc++.h>
#define ll long long
using namespace std;

string s[111];

int n, m;

bool bad(int id) {
    for (int j = 0; j < m; ++j) {
        if (s[id][j] != '?')
            return false;
    }
    return true;
}

int main() {
#ifdef LOCAL
    freopen("xxx.in", "r", stdin);
    freopen("xxx.out", "w", stdout);
#endif
    int t;
    cin >> t;
    for (int tt = 0; tt < t; ++tt) {
        cin >> n >> m;
        int id;
        for (int i = 0; i < n; ++i) {
            cin >> s[i];
            if (!bad(i))
                id = i;
        }
        for (int i = id + 1; i < n; ++i) {
            if (bad(i))
                s[i] = s[i - 1];
        }
        for (int i = id - 1; i >= 0; --i) {
            if (bad(i))
                s[i] = s[i + 1];
        }
        for (int i = 0; i < n; ++i) {
            int prev = -1;
            for (int j = 0; j < m; ++j) {
                if (s[i][j] == '?' && prev != -1)
                    s[i][j] = s[i][prev];
                if (s[i][j] != '?')
                    prev = j;
            }
            prev = -1;
            for (int j = m - 1; j >= 0; --j) {
                if (s[i][j] == '?' && prev != -1)
                    s[i][j] = s[i][prev];
                if (s[i][j] != '?')
                    prev = j;
            }
        }
        cout << "Case #" << tt + 1 << ":\n";
        for (int i = 0; i < n; ++i)
            cout << s[i] << "\n";
    }    
    return 0;
}