#include <iostream>
#include <utility>
#include <cstdint>
#include <algorithm>
#include <map>
#include <iterator>
#include <iomanip>
typedef std::pair<int, int> ii;

int N, Q;
const int MAXN = 128;
const int MAXQ = 128;
int E[MAXN], S[MAXN];
ii query[MAXQ];
long long distance[MAXN][MAXN];
long long path[MAXN][MAXN];
const long long INF = 1000000002LL*256LL;

double TINF = INF;
double ttr[MAXN][MAXN];

void solve()
{
    for (int i=0; i<N; i++)
        for (int j=0; j<N; j++) path[i][j] = INF;
    
    for (int i=0; i<N; i++)
        path[i][i] = 0;
    
    
    for (int i=0; i<N; i++)
    {
        for (int j=0; j<N; j++)
        {
            if (distance[i][j] != -1) path[i][j] = distance[i][j];
        }
    }
    
    for (int k=0; k<N; k++)
    {
        for (int i=0; i<N; i++)
        {
            for (int j=0; j<N; j++)
            {
                long long dt = path[i][k] + path[k][j];
                path[i][j] = std::min(path[i][j], dt);
            }
        }
    }
    /*
    for (int i=0; i<N; i++)
    {
        for (int j=0; j<N; j++) std::cerr << " " <<  path[i][j] ;
        std::cerr << "\n";
    }
    */
    for (int i=0; i<N; i++)
        for (int j=0; j<N; j++) ttr[i][j] = -1;
    
    for (int i=0; i<N; i++)
        ttr[i][i] = 0;
    
    for (int i=0; i<N; i++)
    {
        for (int j=0; j<N; j++)
        {
            if (E[i] >= path[i][j])
            {
                ttr[i][j] = (double)path[i][j] / S[i];
            }
        }
    }
    
    for (int k=0; k<N; k++)
    {
        for (int i=0; i<N; i++)
        {
            for (int j=0; j<N; j++)
            {
                if (ttr[i][k] < 0 || ttr[k][j] < 0) continue;
                double tp = ttr[i][k] + ttr[k][j];
                if (ttr[i][j] < 0 || tp < ttr[i][j])
                {
                    ttr[i][j] = tp;
                }
            }
        }
    }
    /*
      for (int i=0; i<N; i++)
    {
        for (int j=0; j<N; j++) std::cerr << " " <<  ttr[i][j] ;
        std::cerr << "\n";
    }*/
}

int main()
{
    int t;
    std::cin >> t;
    for (int i=1; i<=t; i++)
    {
        std::cin >> N >> Q;
        for (int j=0; j<N; j++) std::cin >> E[j] >> S[j];
        for (int j=0; j<N; j++)
        {
            for (int k=0; k<N; k++)
            {
                std::cin >> distance[j][k];
            }
        }
        for (int j=0; j<Q; j++)
        {
            int a, b;
            std::cin >> a >> b;
            a--;
            b--;
            query[j] = ii(a, b);
        }
        solve();
        std::cout << "Case #" << i << ":";
        for (int j=0; j<Q; j++)
        {
            std::cout << " "  << std::fixed << std::setprecision(7) << ttr[query[j].first][query[j].second];
        }
        std::cout << "\n";
        
    }
}
