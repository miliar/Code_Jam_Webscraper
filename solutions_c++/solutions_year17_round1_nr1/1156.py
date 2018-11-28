#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using llint = long long;
#define FOR(i, a, b) for(int i = a; i <= b; ++i)
#define REP(i, n)    FOR(i, 0, n - 1)

char c[100][100];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, R, C;
    cin >> T;
    REP(t, T) {
        cin >> R >> C;
        FOR(i, 1, R) {
            string s;
            cin >> s;
            FOR(j, 1, C) {
                c[i][j] = s[j - 1];
            }
        }

        FOR(i, 1, R) {
            FOR(j, 1, C) {
                if (c[i][j] != '?') {
                    int k = j;
                    while (k - 1 > 0 && c[i][k - 1] == '?') {
                        k -= 1;
                        c[i][k] = c[i][k + 1];
                    }
                    k = j;
                    while (k + 1 <= C && c[i][k + 1] == '?') {
                        k += 1;
                        c[i][k] = c[i][k - 1];
                    }
                }
            }
        }

        FOR(i, 1, R) {
            FOR(j, 1, C) {
                if (c[i][j] != '?') {
                    int k = i;
                    while (k - 1 > 0 && c[k - 1][j] == '?') {
                        k -= 1;
                        c[k][j] = c[k + 1][j];
                    }
                    k = i;
                    while (k + 1 <= R && c[k + 1][j] == '?') {
                        k += 1;
                        c[k][j] = c[k - 1][j];
                    }
                }
            }
        }

        cout << "Case #" << t + 1 << ":\n";
        FOR(i, 1, R) {
            FOR(j, 1, C) {
                cout << c[i][j];
            }
            cout << "\n";
        }
    }
    fclose(stdout);
}
