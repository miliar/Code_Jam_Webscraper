#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using llint = long long;
#define FOR(i, a, b) for(int i = a; i <= b; ++i)
#define REP(i, n)    FOR(i, 0, n - 1)

bool intersect(int a, int b, int c, int d) {
    int r;
    if (a > c) {
        r = a; a = c; c = r;
        r = b; b = d; d = r;
    }
    return c <= b && a <= b && c <= d;
}

int N, P, R[50], Q[50][50], lower[50][50], upper[50][50], ne[50][50][2], fr[50][50];

int trial(int i, int j) {
    int l = ne[i][j][0];
    int r = ne[i][j][1];

    if (i == N - 1) {
        fr[i][j] = 1;
        return 1;
    }

    if (fr[i][j] == 1 || l > r) {
        return 0;
    }
    fr[i][j] = 1;
    FOR(k, l, r) {
        if (trial(i + 1, k)) {
            return 1;
        }
    }
    fr[i][j] = 0;
    return 0;
}

int up(double n) {
    int u = n;
    n -= int(n);
    if (n > 0.0) {
       u += 1;
    }
    return u;
}

int main() {
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);
    int T;
    cin >> T;
    REP(t, T) {
        cin >> N >> P;
        memset(fr, 0, sizeof(fr));
        REP(i, N) {
            cin >> R[i];
        }
        REP(i, N) {
            REP(j, P) {
                cin >> Q[i][j];
            }
            sort(Q[i], Q[i] + P);
            REP(j, P) {
                lower[i][j] = max(1, up(Q[i][j] / 1.1/ R[i]));
                upper[i][j] = (Q[i][j] / 0.9 / R[i]);
            }
        }

        REP(i, N - 1) {
            REP(j, P) {
                ne[i][j][0] = P + 1;
                ne[i][j][1] =  -1;
                REP(k, P) {
                    if (intersect(lower[i][j], upper[i][j], lower[i + 1][k], upper[i + 1][k])) {
                        ne[i][j][0] = min(ne[i][j][0], k);
                        ne[i][j][1] = max(ne[i][j][1], k);
                    }
                }
            }
        }


        int res = 0;
        REP(j, P) {
            if (lower[0][j] <= upper[0][j])
               res += trial(0, j);
        }
        cout << "Case #" << t + 1 << ": " << res << "\n";
    }
    fclose(stdout);
}
