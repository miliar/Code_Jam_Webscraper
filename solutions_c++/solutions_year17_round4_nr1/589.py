#include "iostream"
#include "cstdio"
#include "cstdlib"
#include "string.h"
#include "vector"
#include "map"
#include "set"
#include "algorithm"
#include "queue"
#include "cmath"
#include <typeinfo>
#include "unordered_set"

#define ll long long
#define ull unsigned long long

std::map<ll, int> dp;

int p;

ll gethash(int x, int y, int z, int k)
{
    return 1LL * x * 101 * 101 * 101
            + 1LL * y * 101 * 101
            + 1LL * z * 101
            + k;
}

int dfs(int x, int y, int z, int k)
{
    if (x < 0 || y < 0 || z < 0 || k < 0)
    {
        return 0;
    }
    ll ha = gethash(x, y, z, k);
    if (dp.find(ha) != dp.end())
    {
        return dp[ha];
    }
    int shit = (y + 2*z + 3*k) % p == 0 ? 1 : 0;
    int ans = shit + std::max(dfs(x-1, y, z, k), std::max(dfs(x, y-1, z, k), std::max(dfs(x, y, z-1, k), dfs(x, y, z, k-1))));
    //std::cout << x << " " << y << " " << z << " " << ans << std::endl;
    return dp[ha] = ans;
}


int main()
{
    freopen("A-large (2).in", "r", stdin);
//    freopen("C-large (1).in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, cas = 1;
    scanf("%d", &T);
    while(T--)
    {
        dp.clear();
        int x = 0, y = 0, z = 0, k = 0;
        int n;
        scanf("%d%d", &n, &p);
        for (int i = 0; i < n; i++)
        {
            int pp;
            scanf("%d", &pp);
            int shit = pp % p;
            if (shit == 0) x++;
            else if (shit == 1) y++;
            else if (shit == 2) z++;
            else if (shit == 3) k++;
        }
        int oo = 0;
        if ((y + z*2 + 3*k) % p == 0) oo = -1;
        printf("Case #%d: %d\n", cas++, dfs(x, y, z, k) + oo);
    }
	return true;
}
