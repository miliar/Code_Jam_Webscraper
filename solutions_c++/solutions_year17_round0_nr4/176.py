#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <string>
#include <cstring>
#include <complex>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
#define mp make_pair

const int N = 222;
int s;
int n;
char initial[N][N];
char answer[N][N];
bool g[N][N];
int mtx[N], mty[N];
bool used[N];

void read()
{
    int m;
    scanf("%d%d", &s, &m);
    for (int i = 0; i < s; i++)
        for (int j = 0; j < s; j++)
            initial[i][j] = '.';
    while(m--)
    {
        char c;
        int x, y;
        scanf(" %c %d%d", &c, &x, &y);
        x--;y--;
        initial[x][y] = c;
    }
    for (int i = 0; i < s; i++)
        for (int j = 0; j < s; j++)
            answer[i][j] = initial[i][j];
    return;
}

void modify(int x, int y, int t)
{
    if (t == 0)
    {
        if (answer[x][y] == '.')
            answer[x][y] = 'x';
        else
            answer[x][y] = 'o';
    }
    else
    {
        if (answer[x][y] == '.')
            answer[x][y] = '+';
        else
            answer[x][y] = 'o';
    }
}

bool dfs(int x)
{
    if (used[x]) return false;
    used[x] = 1;
    for (int y = 0; y < n; y++)
    {
        if (!g[x][y]) continue;
        if (mty[y] == -1 || dfs(mty[y]))
        {
            mtx[x] = y;
            mty[y] = x;
            return true;
        }
    }
    return false;
}

void kuhn()
{
    for (int i = 0; i < n; i++)
    {
        mtx[i] = mty[i] = -1;
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            used[j] = 0;
        dfs(i);
    }
    return;
}

void printAns()
{
    int sc = 0, ch = 0;
    for (int i = 0; i < s; i++)
        for (int j = 0; j < s; j++)
        {
            ch += (int)(answer[i][j] != initial[i][j]);
            if (answer[i][j] == '+' || answer[i][j] == 'x')
                sc += 1;
            else if (answer[i][j] == 'o')
                sc += 2;
        }
    printf("%d %d\n", sc, ch);
    for (int i = 0; i < s; i++)
        for (int j = 0; j < s; j++)
        {
            if (answer[i][j] == initial[i][j]) continue;
            printf("%c %d %d\n", answer[i][j], i + 1, j + 1);
        }
    return;
}

void solve()
{
    n = s;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            g[i][j] = 1;
    for (int i = 0; i < n; i++)
    {
        bool ok = true;
        for (int j = 0; j < n; j++)
            ok &= (initial[i][j] == '.' || initial[i][j] == '+');
        for (int j = 0; j < n; j++)
            g[i][j] &= ok;
    }
    for (int j = 0; j < n; j++)
    {
        bool ok = true;
        for (int i = 0; i < n; i++)
            ok &= (initial[i][j] == '.' || initial[i][j] == '+');
        for (int i = 0; i < n; i++)
            g[i][j] &= ok;
    }
    kuhn();
    for (int x = 0; x < n; x++)
    {
        if (mtx[x] == -1) continue;
        int y = mtx[x];
        modify(x, y, 0);
    }
    n = 2 * s;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            g[i][j] = 0;
    for (int x = 0; x < s; x++)
        for (int y = 0; y < s; y++)
        {
            int v = x + y;
            int u = x - y + s;
            g[v][u] = 1;
        }
    for (int i = 0; i < n; i++)
    {
        bool ok = true;
        for (int x = 0; x < s; x++)
        {
            int y = i - x;
            if (y < 0 || y >= s) continue;
            ok &= (initial[x][y] == '.' || initial[x][y] == 'x');
        }
        for (int j = 0; j < n; j++)
            g[i][j] &= ok;
    }
    for (int j = 0; j < n; j++)
    {
        bool ok = true;
        for (int x = 0; x < s; x++)
        {
            int y = x + s - j;
            if (y < 0 || y >= s) continue;
            ok &= (initial[x][y] == '.' || initial[x][y] == 'x');
        }
        for (int i = 0; i < n; i++)
            g[i][j] &= ok;
    }
    kuhn();
    for (int i = 0; i < n; i++)
    {
        if (mtx[i] == -1) continue;
        int j = mtx[i];
        int x = (i + j - s) / 2;
        int y = i - x;
        modify(x, y, 1);
    }
    printAns();
    return;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        printf("Case #%d: ", i + 1);
        read();
        solve();
    }

    return 0;
}
