#include <bits/stdc++.h>

using namespace std;

int n, q, e[101], o[101], s[101];
double ans, g[101][101];
bool used[101];

void dfs(int u, int v, int hno = -1, double res = 0) {
    //cout << u << " " << v << " " << hno << " " << res << "\n";
    if (u == v) {
        if (res < ans) ans = res;
        return;
    }

    for (int i = 0; i < n; ++i) {
        if (g[u][i] != -1) {
            if (hno >= 0 && o[hno] >= g[u][i]) {
                o[hno] -= g[u][i];
                used[u] = true;
                dfs(i, v, hno, res + g[u][i] / s[hno]);
                o[hno] += g[u][i];
                used[u] = false;
            }
            if (o[u] >= g[u][i]) {
                o[u] -= g[u][i];
                used[u] = true;
                dfs(i, v, u, res + g[u][i] / s[u]);
                o[u] += g[u][i];
                used[u] = false;
            }
        }
    }
}

void true_main (int test) {
    cin >> n >> q;

    for (int i = 0; i < n; ++i) cin >> e[i] >> s[i];

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> g[i][j];
        }
    }

    cout << "Case #" << test << ": ";
    cout.precision(6);

    for (int i = 0; i < q; ++i) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        ans = 1e18;
        for (int i = 0; i < n; ++i) {
            o[i] = e[i];
        }

        dfs(u, v);

        cout << fixed << ans << " ";
    }

    cout << "\n";

}

/*void true_main (int test) {
    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;

    cout << "Case #" << test << ": ";
    if (o + r > n / 2 || o + y > n / 2) {
        cout << "IMPOSSIBLE\n";
        return;
    }
    if (g + y > n / 2 || g + b > n / 2) {
        cout << "IMPOSSIBLE\n";
        return;
    }
    if (v + r > n / 2 || v + b > n / 2) {
        cout << "IMPOSSIBLE\n";
        return;
    }

    vector<char> cols, c1, c2;

    for (int i = 0; i < r; ++i) {
        cols.push_back('r');
        c1.push_back('r');
        c2.push_back('r');
    }
    for (int i = 0; i < g; ++i) {
        cols.push_back('g');
        c1.push_back('y');
        c2.push_back('b');
    }
    for (int i = 0; i < b; ++i) {
        cols.push_back('b');
        c1.push_back('b');
        c2.push_back('b');
    }
    for (int i = 0; i < y; ++i) {
        cols.push_back('y');
        c1.push_back('y');
        c2.push_back('y');
    }
    for (int i = 0; i < o; ++i) {
        cols.push_back('o');
        c1.push_back('r');
        c2.push_back('y');
    }
    for (int i = 0; i < v; ++i) {
        cols.push_back('v');
        c1.push_back('y');
        c2.push_back('b');
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (c1[i] == c1[j] || c2[i] == c1[j] || c1[i] == c2[j] || c2[i] == c2[j]) {
                g[i][j] = 0;
            }
            else {
                g[i][j] = 1;
                cnt[i]++;
                cnt[j]++;
            }
        }
    }

    for
}*/

main () {
#define FILES
#ifdef FILES
    freopen("C-small-attempt2.in", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t) {
        true_main(t);
    }
}
