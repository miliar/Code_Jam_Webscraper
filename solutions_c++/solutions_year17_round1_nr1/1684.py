#include <bits/stdc++.h>

using namespace std;

#define REP(i, N) for (int (i) = 0; (i) < (N); ++(i))
#define READALL(c) for (auto &e : c) { cin >> e; }
#define PRINTALL(c) for (const auto &e : c) { cout << e << "\t"; } cout << "\n";

template <typename T>
using V = vector<T>;

int R, C;
V<string> G;

void fill(int r, int c) {
    char initial = G[r][c];
    int i = c-1, j = c+1;
    while (i >= 0 && G[r][i] == '?') {
        --i;
    }
    while (j < C && G[r][j] == '?') {
        ++j;
    }
    ++i; --j;
    int a = r-1, b = r+1;
    while (a >= 0) {
        bool g = 1;
        for (int k = i; k <= j; ++k) {
            if (G[a][k] != '?') {
                g = 0;
                break;
            }
        }
        if (!g || a < 0)
            break;
        --a;
    }
    ++a;

    while (b < R) {
        bool g = 1;
        for (int k = i; k <= j; ++k) {
        	// cout << b << " " << k << " " << G[b][k] << " " << initial << endl;
            if (G[b][k] != '?') {
            	// cout << "yee" << endl;
                g = 0;
                break;
            }
        }
        if (!g || b >= R)
            break;
        ++b;
    }
    --b;

    // cout << initial << " " << a << " " << b << endl;

    for (int r1 = a; r1 <= b; ++r1) {
        for (int c1 = i; c1 <= j; ++c1) {
            G[r1][c1] = initial;
        }
    }
}

void solve() {
    cin >> R >> C;
    G.resize(R);
    READALL(G);
    set<char> done = {'?'};
    REP(i, R) {
        REP(j, C) if (!done.count(G[i][j])) {
            fill(i, j);
            done.insert(G[i][j]);
        }
    }
    cout << endl;
    REP(i, R) {
        REP(j, C) {
            cout << G[i][j];
        }
        cout << endl;
    }

}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    REP(tc, T) {
        cout << "Case #" << (tc+1) << ": ";
        solve();
    }
}