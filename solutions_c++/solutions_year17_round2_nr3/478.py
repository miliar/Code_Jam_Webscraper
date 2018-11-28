#include <bits/stdc++.h>

using namespace std;

int main() {
//    freopen("sample.in", "r", stdin);
//    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    for (int ti = 1; ti <= tc; ++ti) {
        printf("Case #%d: ", ti);

        int n, q;
        cin >> n >> q;
        vector<int> e(n);
        vector<int> s(n);
        for (int i = 0; i < n; ++i) {
            cin >> e[i] >> s[i];
        }
        vector<vector<int>> d(n, vector<int>(n));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> d[i][j];
            }
        }
        for (int i = 0; i < q; ++i) {
            int u, v;
            cin >> u >> v;
            --u; --v;
            set<tuple<double, int, int, int>> q;
            q.insert(make_tuple(0, u, e[u], s[u]));
            vector<vector<double>> mt(1001, vector<double>(n, 1e18));
            mt[s[u]][u] = 0;
            do {
                auto top = q.begin();
                double t = get<0>(*top);
                int city = get<1>(*top);
                int energy = get<2>(*top);
                int speed = get<3>(*top);
                q.erase(top);

                for (int to = 0; to < n; ++to) {

                    if (d[city][to] == -1) {
                        continue;
                    }

                    if (d[city][to] <= energy) {
                        double tt = d[city][to] / (double) speed;
                        if (t+tt < mt[speed][to]) {
                            mt[speed][to] = t+tt;
                            q.insert(make_tuple(t+tt, to, energy - d[city][to], speed));
                        }
                    }

                    if (d[city][to] > e[city]) {
                        continue;
                    }

                    double tt = d[city][to] / (double) s[city];

                    if (t+tt < mt[s[city]][to]) {
                        mt[s[city]][to] = t+tt;
                        q.insert(make_tuple(t+tt, to, e[city]-d[city][to], s[city]));
                    }
                }
            }
            while (!q.empty());
            double minAnswer = 1e18;
            for (int i = 1; i < 1001; ++i)
                minAnswer = min(minAnswer, mt[i][v]);
            printf("%.7lf ", minAnswer);
        }
        printf("\n");
    }
    return 0;
}
