/// Bismillahir Rahmanir Rahim

/// Pure_Protea

#include <bits/stdc++.h>
using namespace std;
typedef long long lng;
const double PI = acos(-1.0);
inline int getInt()
{
    int x;
    scanf("%d", &x);
    return x;
}
#define II getInt()
#define dbg(x) cerr << #x << " -->  " << x << endl;
#define theromeo421 main()
#define min3(x,y,z) min(x, min(y, z))
#define read(a) freopen(a, "r", stdin);
#define write(a) freopen(a, "w", stdout);

const int inf = 1 << 30;

void solve();


void IO()
{
    read("C-small-attempt0.in");
    write("out.txt");
}

int theromeo421
{
    IO();

    int T = II;
    cerr << T << " Cases to be completed" << endl << endl;
    for(int cas = 1; cas <= T; ++cas)
    {
        printf("Case #%d: ", cas);
        solve();
        cerr << cas << " Done" << endl;
    }
    return 0;
}

const int N = 101;
int mat[N][N], E[N], S[N];
double A[N], dis[N];

void solve()
{
    for(int i = 0; i < N; ++i)
    {
        A[i] = (double)(1LL << 62);
        dis[i] = 0.0;
    }
    A[1] = 0.0;
    int n = II, q = II;
    for(int i = 1; i <= n; ++i)
    {
        E[i] = II;
        S[i] = II;
    }
    for(int i = 1; i <= n; ++i)
    {
        for(int j = 1; j <= n; ++j)
        {
            mat[i][j] = II;
        }
    }
    for(int i = 2; i <= n; ++i)
    {
        dis[i] = dis[i - 1] + (double)(mat[i - 1][i]);
    }
    while(q--)
    {
        int u = II, v = II;
        for(int i = 1; i < n; ++i) /// i'th horse
        {
            for(int j = i + 1; j <= n; ++j) /// j'th city
            {
                if(dis[j] - dis[i] <= (double)E[i])
                {
                    A[j] = min(A[j], A[i] + (dis[j] - dis[i]) / (double)S[i]);
                }
            }
        }
        printf("%0.7f\n", A[v]);
        cerr << A[v] << endl;
    }
}
