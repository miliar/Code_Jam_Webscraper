#include <bits/stdc++.h>
using namespace std;
int n, m;
const int N = 55;
int A[N];
struct node {int l, r;} L[N][N];
int comp(node a, node b)
{
    return (a.r == b.r? a.l < b.l: a.r < b.r);
}
int ls[N];
int main()
{
    int T;
    scanf("%d", &T);
    int P = 0;
    while (T --)
    {
        P ++;
        scanf("%d%d", &n, &m);
        for (int i = 1; i <= n; ++ i)
            scanf("%d", &A[i]);
        for (int i = 1; i <= n; ++ i)
        {
            for (int j = 1; j <= m; ++ j)
            {
                int a;
                scanf("%d", &a);
                int l = ceil(1.0 * (10 * a) / (11 * A[i]) - 1e-12), r = floor(1.0 * (10 * a) / (9 * A[i]) + 1e-12);
                L[i][j] = (node){l, r};
            }
            sort(L[i] + 1, L[i] + m + 1, comp);
            ls[i] = 1;
        }
        int ans = 0;
        while (1)
        {
            for (int i = 1; i <= n; ++ i)
                if (ls[i] == m + 1) goto putttt;
            int rmn = 1, lmx = 1;
            for (int i = 2; i <= n; ++ i)
            {
                if (L[i][ls[i]].l > L[lmx][ls[lmx]].l) lmx = i;
                if (L[i][ls[i]].r < L[rmn][ls[rmn]].r) rmn = i;
            }
            if (L[lmx][ls[lmx]].l <= L[rmn][ls[rmn]].r)
            {
                ans ++;
                for (int i = 1; i <= n; ++ i) ls[i] ++;
            }
            else
            {
                ls[rmn] ++;
            }
        }
        putttt:printf("Case #%d: ", P);
        printf("%d\n", ans);
    }
}
