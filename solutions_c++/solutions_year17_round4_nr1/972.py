#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define MAXN 103
#define MAXP 4
int f2[2][MAXN][MAXN];
int f3[3][MAXN][MAXN][MAXN];
int f4[4][MAXN][MAXN][MAXN][MAXN];
int n, p;
int a[MAXP];
int dfs2(int m, int a0, int a1)
{
    if (a0 == 0 && a1 == 0)
        return 0;
    int &ans = f2[m][a0][a1];
    if (ans != -1)
        return ans;
    if (a0)
        ans = dfs2(m, a0 - 1, a1) + (m == 0);
    if (a1)
        ans = max(ans, dfs2(1 - m, a0, a1 - 1) + (m == 0));
    return ans;
}
int dfs3(int m, int a0, int a1, int a2)
{
    if (a0 == 0 && a1 == 0 && a2 == 0)
        return 0;
    if (m < 0)
        m += 3;
    int &ans = f3[m][a0][a1][a2];
    if (ans != -1)
        return ans;
    if (a0)
        ans = dfs3(m, a0 - 1, a1, a2) + (m == 0);
    if (a1)
        ans = max(ans, dfs3(m - 1, a0, a1 - 1, a2) + (m == 0));
    if (a2)
        ans = max(ans, dfs3(m - 2, a0, a1, a2 - 1) + (m == 0));
    return ans;
}
int dfs4(int m, int a0, int a1, int a2, int a3)
{
    if (a0 == 0 && a1 == 0 && a2 == 0 && a3 == 0)
        return 0;
    if (m < 0)
        m += 4;
    int &ans = f4[m][a0][a1][a2][a3];
    if (ans != -1)
        return ans;
    if (a0)
        ans = dfs4(m, a0 - 1, a1, a2, a3) + (m == 0);
    if (a1)
        ans = max(ans, dfs4(m - 1, a0, a1 - 1, a2, a3) + (m == 0));
    if (a2)
        ans = max(ans, dfs4(m - 2, a0, a1, a2 - 1, a3) + (m == 0));
    if (a3)
        ans = max(ans, dfs4(m - 3, a0, a1, a2, a3 - 1) + (m == 0));
    return ans;
}
int main()
{
    int T;
    scanf("%d", &T);
    for (int Ti = 1; Ti <= T; ++Ti) {
        scanf("%d%d", &n, &p);
        memset(a, 0, sizeof(a));
        for (int i = 0; i < n; ++i) {
            int x;
            scanf("%d", &x);
            a[x % p]++;
        }
        printf("Case #%d: ", Ti);
        if (p == 2) {
            memset(f2, 0xff, sizeof(f2));
            printf("%d\n", dfs2(0, a[0], a[1]));
        }
        if (p == 3) {
            memset(f3, 0xff, sizeof(f3));
            printf("%d\n", dfs3(0, a[0], a[1], a[2]));
        }
        if (p == 4) {
            memset(f4, 0xff, sizeof(f4));
            printf("%d\n", dfs4(0, a[0], a[1], a[2], a[3]));
        }
    }
    return 0;
}
