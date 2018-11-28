#include <bits/stdc++.h>

using namespace std;

#define N 100

char dict[] = { '.', '+', 'x', '.', 'o' };

typedef struct ANStype {
    char c; int i, j;
    ANStype(int v, int i, int j) {
        this->i = i + 1, this->j = j + 1;
        this->c = dict[v];
    }
} ANS;

int m, n, data[N][N], perm[N][N];
bool occ_row[N], occ_col[N], occ_rl[2 * N - 1], occ_lr[2 * N - 1];
int ans = 0; vector<ANS> sol, msol;

// o = 4, x = 2, + = 1

inline int find_row(int i, int j) { return i; }
inline int find_col(int i, int j) { return j; }
inline int find_rl(int i, int j) { return i + j; }
inline int find_lr(int i, int j) { return j - i + n - 1; }
inline int value(int v) { return v == 4 ? 2 : (v == 0 ? 0 : 1); }

inline void update(int i, int j, int v) {
    if (v == 4 || v == 1) {
        // cout << "occ_rl" << find_rl(i, j) << "=true" << endl;
        occ_rl[find_rl(i, j)] = true;
        occ_lr[find_lr(i, j)] = true;
    }
    if (v == 4 || v == 2) {
        // cout << "occ_row" << find_row(i, j) << "=true" << endl;
        // cout << "occ_col" << find_col(i, j) << "=true" << endl;
        occ_row[find_row(i, j)] = true;
        occ_col[find_col(i, j)] = true;
    }
}

inline void put(int i, int j, int v) {
    int r = find_row(i, j), c = find_col(i, j), lr = find_lr(i, j), rl = find_rl(i, j);
    bool br = occ_row[r], bc = occ_col[c], blr = occ_lr[lr], brl = occ_rl[rl];
    // cout << v << " " << i << j << endl;
    if (v == 4) {
        if (data[i][j] == 1) assert(!br && !bc);
        if (data[i][j] == 2) assert(!blr && !brl);
    } else {
        assert(v == 1 || (!br && !bc));
        assert(v == 2 || (!blr && !brl));
    }
    ans += value(v) - value(data[i][j]);
    update(i, j, data[i][j] = v);
    msol.push_back(ANStype(v, i, j));
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t, a, b; char c; int cur = 0;
    cin >> t;
    for (int it = 1; it <= t; it++) {
        cin >> n >> m;
        for (int i = 0; i < n; i++)
            memset(data[i], 0, n * sizeof(int));
        memset(occ_row, false, n * sizeof(int));
        memset(occ_col, false, n * sizeof(int));
        memset(occ_rl, false, (2 * n - 1) * sizeof(int));
        memset(occ_lr, false, (2 * n - 1) * sizeof(int));
        cur = 0;
        for (int i = 1; i <= m; i++) {
            cin >> c >> a >> b;
            a--, b--;
            if (c == 'o') data[a][b] = 4;
            else if (c == 'x') data[a][b] = 2;
            else if (c == '+') data[a][b] = 1;
            update(a, b, data[a][b]);
            // cout << "c = " << c << " val = " << value(c) << endl;
            cur += value(data[a][b]);
        }
        msol.clear();
        ans = cur;
        int u = -1;
        for (int i = 0; i < n; i++) {
            if (data[0][i] == 2 || data[0][i] == 4) {
                u = i; break;
            }
        }
        if (u == -1) {
            u = 0;
            put(0, u, 4);
        }
        if (data[0][u] == 2)
            put(0, u, 4);
        for (int i = 0; i < n; i++)
            if (data[0][i] == 0) put(0, i, 1);
        int tn = -1, tp = 0;
        for (int i = 1; i < n; i++) {
            int tt = (u + i + tp) % n;
            if (tn == -1 && (tt == n - 1 || tt == 0)) {
                put(n - 1, tt, 2);
                tn = tt;
                tp = 1;
                tt = (tt + 1) % n;
            }
            if (i == n - 1) break;
            put(i, tt, 2);
        }
        for (int i = 0; i < n; i++) {
            if (data[n - 1][i] == 0) {
                if (!occ_lr[find_lr(n - 1, i)] && !occ_rl[find_rl(n - 1, i)])
                    put(n - 1, i, 1);
            }
        }
        cout << "Case #" << it << ": " << ans << " " << msol.size() << endl;
        // for (int i = 0; i < n; i++)
        //     for (int j = 0; j < n; j++)
        //         if (data[i][j] == 0) data[i][j] = '.';
        //         else if (data[i][j] == 1) data[i][j] = '+';
        //         else if (data[i][j] == 2) data[i][j] = 'x';
        //         else if (data[i][j] == 4) data[i][j] = 'o';
        for (int i = 0; i < msol.size(); i++) {
            cout << msol[i].c << " " << msol[i].i << " " << msol[i].j << endl;
            // data[msol[i].i - 1][msol[i].j - 1] = msol[i].c;
        }
        // for (int i = 0; i < n; i++ ){
        //     for (int j = 0; j < n; j++)
        //         cout << (char) data[i][j] << " ";
        //     cout << endl;
        // }
    }
    return 0;
}
