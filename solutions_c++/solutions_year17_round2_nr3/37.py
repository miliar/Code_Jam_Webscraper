#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <unordered_set>
#include <unordered_map>
using namespace std;

inline bool update(long long &a, long long b)
{
    if (a == -1 || a > b) {
        a = b;
        return true;
    }
    return false;
}

const double EPS = 1e-8;

int main()
{
    int tests, test = 1;
    for (scanf("%d", &tests); test <= tests; ++ test) {
        int n, q;
        scanf("%d%d", &n, &q);
        vector<int> E(n), S(n);
        for (int i = 0; i < n; ++ i) {
            scanf("%d%d", &E[i], &S[i]);
        }
        vector<vector<long long>> d(n, vector<long long>(n));
        for (int i = 0; i < n; ++ i) {
            for (int j = 0; j < n; ++ j) {
                scanf("%I64d", &d[i][j]);
            }
            d[i][i] = 0;
        }
        for (int k = 0; k < n; ++ k) {
            for (int i = 0; i < n; ++ i) {
                if (d[i][k] != -1) {
                    for (int j = 0; j < n; ++ j) {
                        if (d[k][j] != -1) {
                            update(d[i][j], d[i][k] + d[k][j]);
                        }
                    }
                }
            }
        }

        vector<vector<pair<int, double>>> adj(n);
        for (int u = 0; u < n; ++ u) {
            for (int v = 0; v < n; ++ v) {
                if (u != v && d[u][v] != -1 && d[u][v] <= E[u]) {
                    double cost = d[u][v] / (double)S[u];

                    if (d[u][v] < 0) {
                        cerr << d[u][v] << " " << S[u] << " "<< cost << endl;
                    }

                    adj[u].push_back(make_pair(v, cost));
                }
            }
        }

        printf("Case #%d:", test);

        while (q --) {
            int start, end;
            scanf("%d%d", &start, &end);
            -- start; -- end;

            vector<double> f(n, 1e100);
            vector<bool> mark(n, false);
            f[start] = 0;
            queue<int> q;
            q.push(start);
            while (q.size()) {
                int u = q.front();
                q.pop();
                mark[u] = false;
                for (pair<int, double> edge : adj[u]) {
                    int v = edge.first;
                    double cost = edge.second;
                    if (f[v] > f[u] + cost + EPS) {
                        f[v] = f[u] + cost + EPS;
                        if (!mark[v]) {
                            mark[v] = true;
                            q.push(v);
                            if (f[q.back()] + EPS < f[q.front()]) {
                                swap(q.front(), q.back());
                            }
                        }
                    }
                }
            }
            printf(" %.10f", f[end]);
        }
        puts("");
    }
    return 0;
}
