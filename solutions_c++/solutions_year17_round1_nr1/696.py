#include <bits/stdc++.h>

using namespace std;

#define ll long long

int TEST;

void solve() {
    int n, m;
    scanf("%d %d", &n, &m);

    vector<vector<char>> a(n, vector<char>(m));
    vector<pair<int, int>> let(26, {-1, -1});
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            scanf(" %c", &a[i][j]);
            if (a[i][j] != '?') {
                int p = a[i][j] - 'A';
                let[p] = {i, j};
            }
        }
    }

    for (int cur = 0; cur < 26; ++cur) {
        if (let[cur].first != -1) {
            char c = cur + 'A';

            for (int i = let[cur].first - 1; i >= 0; --i) {
                if (a[i][let[cur].second] != '?') {
                    break;
                }
                a[i][let[cur].second] = c;
            }

            for (int i = let[cur].first + 1; i < n; ++i) {
                if (a[i][let[cur].second] != '?') {
                    break;
                }
                a[i][let[cur].second] = c;
            }
        }
    }

    int st = 0;
    for (int j = 0; j < m; ++j) {
        if (a[0][j] != '?') {
            st = j;
            break;
        }
    }

    for (int j = st - 1; j >= 0; --j) {
        for (int i = 0; i < n; ++i) {
            a[i][j] = a[i][j + 1];
        }
    }

    for (int j = st + 1; j < m; ++j) {
        if (a[0][j] == '?') {
            for (int i = 0; i < n; ++i) {
                a[i][j] = a[i][j - 1];
            }
        } 
    }

    printf("Case #%d:\n", TEST);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cout << a[i][j];
        }
        cout << '\n';
    }
}

int main() {
    int t;
    cin >> t;

    for (TEST = 1; TEST <= t; ++TEST) {
        solve();
    }

    return 0;
}
