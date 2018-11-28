#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

int const maxN = 30;

int n, m;
char ar[maxN][maxN];

void solve1(char c)
{
    for (int i = 0; i < n; ++i)
    {
        for (int j = 1; j < m; ++j)
        {
            if (ar[i][j] == '?' && ar[i][j - 1] == c)
            {
                ar[i][j] = c;
            }
        }
    }
    for (int i = 0; i < n; ++i)
    {
        for (int j = m - 2; j >= 0; --j)
        {
            if (ar[i][j] == '?' && ar[i][j + 1] == c)
            {
                ar[i][j] = c;
            }
        }
    }
}

void solve2(char c)
{
    for (int i = 1; i < n; ++i)
    {
        bool good = true;
        for (int j = 0; j < m && good; ++j)
        {
            if (ar[i - 1][j] == c && ar[i][j] != '?')
            {
                good = false;
            }
        }
        if (good)
        {
            for (int j = 0; j < m; ++j)
            {
                if (ar[i - 1][j] == c)
                    ar[i][j] = c;
            }
        }
    }
    for (int i = n - 2; i >= 0; --i)
    {
        bool good = true;
        for (int j = 0; j < m && good; ++j)
        {
            if (ar[i + 1][j] == c && ar[i][j] != '?')
            {
                good = false;
            }
        }
        if (good)
        {
            for (int j = 0; j < m; ++j)
            {
                if (ar[i + 1][j] == c)
                    ar[i][j] = c;
            }
        }
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int tn = 1; tn <= t; ++tn)
    {
        scanf("%d%d\n", &n, &m);
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                scanf("%c", &ar[i][j]);
            }
            scanf("\n");
        }
        for (char c = 'A'; c <= 'Z'; ++c)
        {
            solve1(c);
        }
        for (char c = 'A'; c <= 'Z'; ++c)
        {
            solve2(c);
        }
        printf("Case #%d:\n", tn);
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                printf("%c", ar[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}