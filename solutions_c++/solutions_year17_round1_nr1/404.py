#include <bits/stdc++.h>
using namespace std;

char a[50][50];
bool has[50];

int main(void) {
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++ t) {
        int n, m;
        cin >> n >> m;
        memset(has, false, sizeof(has));
        for (int i = 0; i < n; ++ i) {
            for (int j = 0; j < m; ++ j) {
                cin >> a[i][j];
                if (a[i][j] != '?') has[i] = true;
            }
        }

        for (int i = 0; i < n; ++ i) {
            for (int j = 0; j < m; ++ j) if (a[i][j] != '?') {
                for (int k = 1; k < m; ++ k) {
                    if (j + k < m && a[i][j + k] == '?') a[i][j + k] = a[i][j];
                    else break;
                }
                for (int k = 1; k < m; ++ k) {
                    if (j - k >= 0 && a[i][j - k] == '?') a[i][j - k] = a[i][j];
                    else break;
                }
            }
        }

        for (int i = 0; i < n; ++ i) {
            if (!has[i]) {
                for (int k = 0; k < n; ++ k) if (has[k]) {
                    for (int j = 0; j < m; ++ j) a[i][j] = a[k][j];
                }
                has[i] = true;
            }
        }

        cout << "Case #" << t << ":" << endl;
        for (int i = 0; i < n; ++ i) for (int j = 0; j < m; ++ j) {
            cout << a[i][j];
            if (j == m - 1) cout << endl;
        }

    }

    return 0;
}
