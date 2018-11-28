#include <bits/stdc++.h>
using namespace std;
#define ff(i, a, b) for(int i = a; i <= b; ++ i)
#define fd(i, a, b) for(int i = a; i >= b; -- i)
#define fin "A-small-attempt0.in"
#define fou "A.out"
#define x first
#define y second
typedef pair <int, int> ii;
typedef long long data;
typedef vector <int> vi;
typedef vector <ii> vii;
const int N = 26;

int test, m, n, f[N][N][N][N], tr[N][N][N][N], sum[N][N];
string s[N], st[N];

void read()
{
    cin >> m >> n;
    ff(i, 1, m)
    {
        cin >> s[i];
        st[i] = s[i];
    }
}

inline int get(int x, int y, int u, int v)
{
    return sum[u][v] - sum[x - 1][v] - sum[u][y - 1] + sum[x - 1][y - 1];
}

int F(int x, int y, int u, int v)
{
    int &res = f[x][y][u][v];
    if (res > -1) return res;
    if (get(x, y, u, v) == 1)
    {
        tr[x][y][u][v] = 0;
        return (res = 1);
    }
    ff(k, x, u - 1) if (F(x, y, k, v) && F(k + 1, y, u, v))
    {
        tr[x][y][u][v] = k;
        return (res = 1);
    }
    ff(k, y, v - 1) if (F(x, y, u, k) && F(x, k + 1, u, v))
    {
        tr[x][y][u][v] = -k;
        return (res = 1);
    }
    return 0;
}

inline void bfill(int x, int y, int u, int v, int c)
{
    ff(i, x, u) ff(j, y, v) st[i][j - 1] = c;
}

void trace(int x, int y, int u, int v)
{
    int k = tr[x][y][u][v];
    if (k == 0)
    {
        char c = '?';
        ff(i, x, u)
            ff(j, y, v)
                if (s[i][j - 1] != '?')
                {
                    c = s[i][j - 1];
                    bfill(x, y, u, v, c);
                    return;
                }
    }
    if (k < 0)
    {
        k = - k;
        trace(x, y, u, k);
        trace(x, k + 1, u, v);
        return;
    }
    else {
        trace(x, y, k, v);
        trace(k + 1, y, u, v);
    }
}

void solve(int tnum)
{
    cout << "Case #" << tnum << ":\n";
    ff(i, 1, m)
        ff(j, 1, n)
            sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + (s[i][j - 1] != '?');
    memset(f, 255, sizeof(f));
    F(1, 1, m, n);
    trace(1, 1, m, n);
    ff(i, 1, m) cout << st[i] << '\n';
}

int main()
{
    ios_base::sync_with_stdio(0);
    //freopen(fin, "r", stdin); freopen(fou, "w", stdout);
    cin >> test;
    ff(i, 1, test)
    {
        read();
        solve(i);
    }
    return 0;
}
