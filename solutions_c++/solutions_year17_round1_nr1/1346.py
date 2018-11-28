#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair <int, int> pii;

#define SZ(c) c.size()
#define ALL(c) c.begin(), c.end()
#define endl '\n'

const int N = 1e5 + 9;

int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "r", stdin);
	freopen("outp.txt", "w", stdout);
#endif

    int cases;
    cin >> cases;
    for (int c = 1; c <= cases; ++c) {
        int n, m;
        cin >> n >> m;

        vector <string> v(n);
        for (int i = 0; i < n; ++i)
            cin >> v[i];

        for (int i = 0; i < n; ++i) {
            char last = '?';
            for (int j = 0; j < m; ++j) {
                if (v[i][j] == '?')
                    v[i][j] = last;
                else last = v[i][j];
            }
            last = '?';
            for (int j = m - 1; j >= 0; --j) {
                if (v[i][j] == '?')
                    v[i][j] = last;
                else last = v[i][j];
            }
        }

        for (int j = 0; j < m; ++j) {
            char last = '?';
            for (int i = 0; i < n; ++i) {
                if (v[i][j] == '?')
                    v[i][j] = last;
                else last = v[i][j];
            }
            last = '?';
            for (int i = n - 1; i >= 0; --i) {
                if (v[i][j] == '?')
                    v[i][j] = last;
                else last = v[i][j];
            }
        }

        cout << "Case #" << c << ":" << endl;
        for (int i = 0; i < n; ++i)
            cout << v[i] << endl;
    }
    return 0;
}
