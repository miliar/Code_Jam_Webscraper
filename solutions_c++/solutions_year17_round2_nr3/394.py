#include <bits/stdc++.h>
using namespace std;
using i64 = int64_t;

struct Tp {
    int x;
    int h;
    i64 f;
};
struct Tp2 {
    int x;
    double t;
};

int main() {
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
    ios::sync_with_stdio(false);

    int T;
    cin >> T;
    for (int __ =1; __ <= T; ++__) {
        int N, Q;
        cin >> N >> Q;

        vector<i64> H(N);
        vector<double> S(N);
        vector<vector<i64>> D(N, vector<i64>(N));

        for (int i = 0; i < N; ++i) {
            cin >> H[i] >> S[i];
        }
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                cin >> D[i][j];
            }
        }

        queue<Tp> q;
        const i64 INF = i64(4e18);
        vector< vector<i64> > f(N, vector<i64>(N, INF));
        for (int i = 0; i < N; ++i) {
            f[i][i] = 0;
            q.push({i, i, 0});
        }
        while (!q.empty()) {
            auto t = q.front(); q.pop();
            int x = t.x;
            int h = t.h;
            i64 ff = t.f;
            if (ff != f[x][h]) {
                continue;
            }

            for (int y = 0; y < N; ++y) {
                if (D[x][y] != -1 && D[x][y] + ff <= H[h] && f[y][h] > ff + D[x][y]) {
                    f[y][h] = ff + D[x][y];
                    q.push({y, h, f[y][h]});
                }
            }
        }

        cout << "Case #" << __ << ":";
        cout.precision(12);
        cout << fixed;

        while (Q-->0) {
            int X, Y;
            cin >> X >> Y;
            --X;
            --Y;

            const double eps = 1e-9;
            queue<Tp2> q;
            vector<double> mint(N, 4e18);
            mint[X] = 0.0;
            q.push({X, mint[X]});

            while (!q.empty()) {
                auto t = q.front(); q.pop();
                int x = t.x;
                auto tt = t.t;
                if ( fabs(mint[x] - tt) > eps) {
                    continue;
                }
                for (int y = 0; y < N; ++y)
                    if (f[y][x] < INF) {
                        double newt = tt + f[y][x] / S[x];
                        if (newt + eps < mint[y]) {
                            mint[y] = newt;
                            q.push({y, newt});
                        }
                    }                        
            }

            cout << ' ' << mint[Y];
        }
        cout << endl;
        cerr << __ << " done" << endl;
    }

    return 0;
}
