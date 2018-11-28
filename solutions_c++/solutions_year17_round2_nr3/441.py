#include <ios>
#include <iostream>
#include <iomanip>
#include <cstdio>
#define INF 1000000000000000000LL

long long int e[105] = {}; //endurance
long long int s[105] = {}; //speed
long long int d[105][105] = {};
double dist[105][105] = {};

inline long long int minimum(long long int a, long long int b)
{
    return (a < b ? a : b);
}

inline double minimum_d(double a, double b)
{
    return (a < b ? a : b);
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc, n, q, u, v;
    std::cin >> tc;
    for (int ttt = 0; ttt < tc; ttt++)
    {
        std::cin >> n >> q;
        for (int i = 0; i < n; i++)
            std::cin >> e[i] >> s[i];
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                std::cin >> d[i][j];
                if (d[i][j] == -1)
                    d[i][j] = INF;
                if (i == j)
                    d[i][j] = 0;
            }
        }
        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    d[i][j] = minimum(d[i][j], d[i][k] + d[k][j]);
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (i == j)
                    dist[i][j] = 0;
                else if (e[i] < d[i][j])
                    dist[i][j] = (double)(INF);
                else
                    dist[i][j] = ((double)(d[i][j]))/(s[i]);
            }
        }
        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    dist[i][j] = minimum_d(dist[i][j], dist[i][k] + dist[k][j]);
        std::cout << "Case #" << ttt+1 << ':';
        while (q--)
        {
            std::cin >> u >> v;
            u--; v--;
            std::cout << ' ' << std::fixed << std::setprecision(9) << dist[u][v];
        }
        std::cout << '\n';
    }
}
