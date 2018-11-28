#include <iostream>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>
#include <cassert>
#include <map>
#include <set>
#include <ctime>
#include <iomanip>
#include <bitset>

using namespace std;

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define sz(X) ((int)((X).size()))

const int N = 100;

int n, m, s[N][N];
char a[N][N];

int count(int n1, int n2, int m1, int m2)
{
    --n1, --m1;
    return s[n2][m2] - s[n2][m1] - s[n1][m2] + s[n1][m1];
}

char find(int n1, int n2, int m1, int m2)
{
    for (int i = n1; i <= n2; ++i)
        for (int j = m1; j <= m2; ++j)
            if (a[i][j] != '?') return a[i][j];
}

void fuck(int n1, int n2, int m1, int m2)
{
    if (count(n1, n2, m1, m2) == 1)
    {
        char c = find(n1, n2, m1, m2);
        for (int i = n1; i <= n2; ++i)
            for (int j = m1; j <= m2; ++j)
                a[i][j] = c;
        return;
    }
    for (int i = n1; i < n2; ++i)
    {
        if (count(n1, i, m1, m2) && count(i + 1, n2, m1, m2))
        {
            fuck(n1, i, m1, m2);
            fuck(i + 1, n2, m1, m2);
            return;
        }
    }
    for (int i = m1; i < m2; ++i)
    {
        if (count(n1, n2, m1, i) && count(n1, n2, i + 1, m2))
        {
            fuck(n1, n2, m1, i);
            fuck(n1, n2, i + 1, m2);
            return;
        }
    }
    while (1);
}

void work()
{
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
        {
            cin >> a[i][j];
            s[i][j] = s[i][j - 1] + s[i - 1][j] - s[i - 1][j - 1] + (a[i][j] != '?');
        }
    fuck(1, n, 1, m);
    for (int i = 1; i <= n; ++i)
    {
        for (int j = 1; j <= m; ++j)
            cout << a[i][j];
        cout << endl;
    }
}

int main()
{
    #ifdef LOCAL_TEST
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i)
    {
        cout << "Case #" << i << ":" << endl;
        work();
    }

    return 0;
}
