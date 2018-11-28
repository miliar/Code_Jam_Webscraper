#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define N 1005
char a[N];
int v[N];
int n, k;

void solve()
{
    scanf("%s%d", a, &k);
    n = strlen(a);
    int s = 0, x = 0;
    memset(v, 0, sizeof(v));
    for (int i = 0; i < n; ++i)
    {
        x += v[i];
        if ((x % 2 && a[i] == '+') || (x % 2 == 0 && a[i] == '-'))
        {
            if (i + k - 1 >= n)
            {
                puts("IMPOSSIBLE");
                return;
            }
            ++s;
            ++x;
            --v[i + k];
        }
    }
    printf("%d\n", s);
}

int main()
{
    int t;
    freopen("1.txt", "r", stdin);
    freopen("2.txt", "w", stdout);
    scanf("%d", &t);
    for (int tt = 1; tt <= t; ++tt)
    {
        printf("Case #%d: ", tt);
        solve();
    }
    return 0;
}