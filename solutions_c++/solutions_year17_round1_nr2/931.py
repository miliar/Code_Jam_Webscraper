#include <bits/stdc++.h>
#define last ost
#define next nst

using namespace std;

const int MaxN = 1e3 + 13;
const int INF = 1e9;

int n, p;
int NEED[MaxN];
int Q[MaxN][MaxN];

pair<int, int> a[MaxN * MaxN];
pair<int, int> b[MaxN * MaxN];
int cost[MaxN * MaxN];
int E[MaxN * MaxN];

int next[MaxN * MaxN];
int last[2][MaxN];

int cnt;

bool used[2][MaxN];

void addOneEdge(int h1, int x1, int h2, int x2, int z)
{
    a[cnt] = make_pair(h1, x1);
    b[cnt] = make_pair(h2, x2);
    cost[cnt] = z;
    if(z)
        E[cnt] = cnt + 1;
    else
        E[cnt] = cnt - 1;
    next[cnt] = last[h1][x1];
    last[h1][x1] = cnt;
}

void addEdge(int h1, int x1, int h2, int x2, int cost)
{
    ++cnt;
    addOneEdge(h1, x1, h2, x2, cost);
    ++cnt;
    addOneEdge(h2, x2, h1, x1, 0);
}

bool dfs(int h, int x)
{
    if(h == 0 && x == n * p + 1)
        return true;
    if(used[h][x])
        return false;
    used[h][x] = true;
    for(int i = last[h][x]; i; i = next[i])
    {
        if(cost[i])
        {

            if(dfs(b[i].first, b[i].second))
            {
                --cost[i];
                ++cost[E[i]];
                return true;
            }
        }
    }
    return false;
}

int getNum(int x, int y)
{
    return y + (x - 1) * p;
}

bool isGood(long long hx, long long x, long long hy, long long y)
{
    x = Q[hx][x];
    y = Q[hy][y];

    long long num = x / (NEED[hx]);

    for(int i = -1000000; i <= 1000000; ++i)
    {
        long long P = num + i;
        if(P > 0)
        {
            long long X = NEED[hx] * P;
            long long Y = NEED[hy] * P;

            if(x * 100 >= X * 90 && x * 100 <= X * 110 && y * 100 >= Y * 90 && y * 100 <= Y * 110)
                return true;
        }
    }
    return false;
}

void solve(int CASE)
{
    cout << "CASE #" << CASE << ": ";
    cin >> n >> p;

    for(int i = 0; i <= p * n + 1; ++i)
        for(int j = 0; j <= 1; ++j)
            last[j][i] = 0;

    for(int i = 0; i <= cnt; ++i)
        next[i] = 0;

    cnt = 0;

    for(int i = 1; i <= n; ++i)
        cin >> NEED[i];

    for(int i = 1; i <= n; ++i)
    {
        for(int j = 1; j <= p; ++j)
            cin >> Q[i][j];
    }

    for(int i = 1; i <= n; ++i)
        for(int j = 1; j <= p; ++j)
        {
            addEdge(0, getNum(i, j), 1, getNum(i, j), 1);
        }

    for(int i = 1; i <= p; ++i)
    {
        if(isGood(1, i, 1, i))
            addEdge(0, 0, 0, getNum(1, i), 1);
        if(isGood(n, i, n, i))
            addEdge(1, getNum(n, i), 0, n * p + 1, 1);
    }

    for(int i = 1; i < n; ++i)
    {
        for(int j = 1; j <= p; ++j)
            for(int j1 = 1; j1 <= p; ++j1)
                if(isGood(i, j, i + 1, j1))
                    addEdge(1, getNum(i, j), 0, getNum(i + 1, j1), 1);
    }

    int ans = 0;

    while(dfs(0, 0))
    {
        ++ans;
        for(int i = 0; i <= n * p + 1; ++i)
            used[0][i] = used[1][i] = false;
    }

    for(int i = 0; i <= n * p + 1; ++i)
        used[0][i] = used[1][i] = false;

    cout << ans << '\n';
    return;
}

main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    for(int t1 = 1; t1 <= t; ++t1)
        solve(t1);
    return 0;
}
