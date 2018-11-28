#include <stdio.h>
#include <iostream>
#include <algorithm>
using LL = long long ;

const LL inf = 1e15;
const double dinf = 1e15;
const int kN = 100 + 5;
int n, nq;
LL e[kN], s[kN];
LL graph[kN][kN];
double t[kN][kN];
double result[kN];

int main()
{
    int cas;
    std::cin >> cas;
    for (int ca = 1; ca <= cas; ++ ca) {
        std::cin >> n >> nq;
        for (int i = 0; i < n; ++ i)
            std::cin >> e[i] >> s[i];
        for (int i = 0; i < n; ++ i) {
            for (int j = 0; j < n; ++ j) {
                std::cin >> graph[i][j];
                if (graph[i][j] == -1)
                    graph[i][j] = inf;
            }
        }
        for (int k = 0; k < n; ++ k)
            for (int i = 0; i < n; ++ i)
                for (int j = 0; j < n; ++ j)
                    graph[i][j] = std::min(graph[i][k] + graph[k][j], graph[i][j]);
        for (int i = 0; i < n; ++ i) {
            for (int j = 0; j < n; ++ j) {
                if (graph[i][j] <= e[i])
                    t[i][j] = graph[i][j] * 1. / s[i];
                else
                    t[i][j] = dinf;
            }
        }
        for (int k = 0; k < n; ++ k)
            for (int i = 0; i < n; ++ i)
                for (int j = 0; j < n; ++ j)
                    t[i][j] = std::min(t[i][k] + t[k][j], t[i][j]);
        for (int i = 0; i < nq; ++ i) {
            int u, v;
            std::cin >> u >> v; u --; v --;
            result[i] = t[u][v];
        }
        printf("Case #%d:", ca);
        for (int i = 0; i < nq; ++ i)
            printf(" %.6f", result[i]);
        puts("");
    }
}
