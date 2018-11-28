#include <bits/stdc++.h>

using namespace std;

#define N 50
int n, p, t, r[N], tt;
pair<int, int> pack[N][N];

pair<int, int> run(int r, int p) {
    int x1 = (10 * p - 0) / (9  * r) + 0;
    int x2 = (10 * p - 1) / (11 * r) + 1;
    return x2 <= x1 ? make_pair(x2, x1) : make_pair(-1, -1);
}

bool cmp(const pair<int, int>& x, const pair<int, int>& y) {
    if (y.second != x.second) return x.second < y.second;
    else return x.first < y.first;
}

int main() {
    // freopen("CodeJam/R1A-2017/B.in", "r", stdin);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> t;
    for (int it = 1; it <= t; it++) {
        cin >> n >> p;
        for (int i = 0; i < n; i++)
            cin >> r[i];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                cin >> tt;
                pack[i][j] = run(r[i], tt);
                // cerr << pack[i][j].first << ", " << pack[i][j].second << " ";
            }
            // cerr << endl;
            sort(pack[i], pack[i] + p, cmp);
        }
        int cur[n], ans = 0;
        memset(cur, 0, n * sizeof(int));
        while (cur[0] < p) {
            const pair<int, int> ax = pack[0][cur[0]];
            if (ax.first == -1) {
                cur[0]++;
                continue;
            }
            bool found = true;
            int curbak[n];
            for (int i = 1; i < n; i++)
                curbak[i] = cur[i];
            for (int i = 1; i < n; i++) {
                while (cur[i] != p) {
                    const pair<int, int> bx = pack[i][cur[i]];
                    if (bx.first == -1)
                        cur[i]++;
                    else if (bx.first <= ax.second && bx.second >= ax.first)
                        break;
                    else if (bx.second < ax.first)
                        cur[i]++;
                    else {
                        found = false;
                        break;
                    }
                }
                if (cur[i] == p) {
                    cur[0] = p;
                    break;
                }
                if (!found) break;
            }
            if (cur[0] == p) break;
            if (found) {
                ans++;
                for (int i = 1; i < n; i++)
                    cur[i]++;
                // cerr << "ans = " << ans << " = ";
                // for (int i = 0; i < n; i++)
                //     cerr << cur[i] << " ";
                // cerr << endl;
            } else {
                for (int i = 1; i < n; i++)
                    cur[i] = curbak[i];
            }
            cur[0]++;
        }
        cout << "Case #" << it << ": " << ans << endl;
    }
    return 0;
}
