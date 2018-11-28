#include <bits/stdc++.h>
#define foru(i, a, b) for (int i = a; i <= b; i++)
using namespace std;
const int MAXN = 105;
const long long INF = 1e18;
int n, q;
long long e[MAXN], s[MAXN], c[MAXN][MAXN];
long double d[MAXN];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int TC;
    scanf("%d", &TC);

    foru(TT, 1, TC) {
        scanf("%d%d", &n, &q);
        foru(i, 1, n) scanf("%I64d%I64d", &e[i], &s[i]);
        foru(i, 1, n) foru(j, 1, n) scanf("%I64d", &c[i][j]);
        foru(i, 1, n) foru(j, 1, n) c[i][j] = i == j ? 0 : (c[i][j] == -1 ? INF : c[i][j]);
        foru(k, 1, n)
            foru(u, 1, n)
                foru(v, 1, n)
                    c[u][v] = min(c[u][v], c[u][k] + c[k][v]);

        //foru(u, 1, n) foru(v, 1, n) cout << u << " " << v << " " << c[u][v] << endl;

        cout << "Case #" << TT << ": ";
        while (q--) {
            int fi, se;
            scanf("%d%d", &fi, &se);
            set<pair<long double, int> > S;
            foru(i, 1, n) d[i] = INF; d[fi] = 0;
            foru(i, 1, n) S.insert(make_pair(d[i], i));
            while (S.size()) {
                int u = S.begin()->second; S.erase(S.begin());
                //cout << u << " " << d[u] << endl;
                if (u == se) {
                    cout << fixed << setprecision(9) << d[u] << " ";
                    break;
                }
                foru(v, 1, n)
                    if (c[u][v] <= e[u] && d[v] > d[u] + 1.0 * c[u][v] / s[u]) {
                        S.erase(S.find(make_pair(d[v], v)));
                        d[v] = d[u] + 1.0 * c[u][v] / s[u];
                        S.insert(make_pair(d[v], v));
                    }
            }
        }
        cout << endl;
    }

}
