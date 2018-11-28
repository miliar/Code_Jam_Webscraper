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

const int N = 30;
char s[N][N];
int n, m;

void solve()
{
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++)
        scanf(" %s ", s[i]);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m - 1; j++)
            if (s[i][j + 1] == '?')
                s[i][j + 1] = s[i][j];
        for (int j = m - 2; j >= 0; j--)
            if (s[i][j] == '?')
                s[i][j] = s[i][j + 1];
    }
    for (int j = 0; j < m; j++)
    {
        for (int i = 0; i < n - 1; i++)
            if (s[i + 1][j] == '?')
                s[i + 1][j] = s[i][j];
        for (int i = n - 1; i >= 0; i--)
            if (s[i][j] == '?')
                s[i][j] = s[i + 1][j];
    }
    for (int i = 0; i < n; i++)
        printf("%s\n", s[i]);
    return;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++)
    {
        printf("Case #%d:\n", i);
        solve();
    }

    return 0;
}
