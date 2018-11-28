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

int const maxN = 1010;
char s[maxN];

void switch_s(int pos, int k)
{
    for (int i = 0; i < k; ++i)
    {
        s[pos + i] = s[pos + i] == '+' ? '-' : '+';
    }
}

int solve()
{
    memset(s, 0, sizeof(s));
    int k;
    scanf("%s%d\n", s, &k);
    int n = strlen(s);
    int ans = 0;
    for (int i = 0; i < n; ++i)
    {
        if (s[i] == '-')
        {
            if (i + k > n)
                return -1;
            switch_s(i, k);
            ans++;
        }
    }
    return ans;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d\n", &t);
    for (int ti = 0; ti < t; ++ti)
    {
        printf("Case #%d: ", ti + 1);
        int res = solve();
        if (res < 0)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", res);
    }
    return 0;
}