#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int n, r, o, y, g, b, v;

void print(char a, int x, char b, int y, char c, int z)
{
    int w = y + z - x;
    for (int i = 0; i < w; ++i)
    {
        putchar(a);
        putchar(b);
        putchar(c);
    }
    y -= w;
    for (int i = 0; i < y; ++i)
    {
        putchar(a);
        putchar(b);
    }
    z -= w;
    for (int i = 0; i < z; ++i)
    {
        putchar(a);
        putchar(c);
    }
    puts("");
}

void solve()
{
    scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
    if (r + y < b || r + b < y || y + b < r)
        puts("IMPOSSIBLE");
    else
    {
        if (r >= y && r >= b)
            print('R', r, 'Y', y, 'B', b);
        else if (y >= r && y >= b)
            print('Y', y, 'R', r, 'B', b);
        else
            print('B', b, 'R', r, 'Y', y);
    }
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