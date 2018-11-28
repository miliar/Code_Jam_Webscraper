#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;

const int maxn = 55;
const int maxp = 55;
const double eps = 1e-8;

int R[maxn];
int q[maxn][maxp], l[maxn][maxp], r[maxn][maxp];
int pos[maxn];

int solve(int n, int p)
{
    memset(pos, 0, sizeof(pos));
    int flag = 0;
    int ans = 0;
    while (1) {
        //printf("!!!!!!\n");
        //for (int i=0;i<n;i++)
        //    printf("%d\n",pos[i]);
        int minr = 100000000, maxl = 0;
        for (int i = 0; i<n;i++)
        {
            minr = min(minr, r[i][pos[i]]);
            maxl = max(maxl, l[i][pos[i]]);
        }
        if (minr >= maxl) {
            ans++;
            for (int i=0;i<n;i++)
                pos[i]++;
        }
        else {
            int posminr = 0;
            for (int i=1;i<n;i++)
                if (r[i][pos[i]] < r[posminr][pos[posminr]]) posminr = i;
            pos[posminr]++;
        }
        for (int i=0;i<n;i++)
            if (pos[i]>=p) return ans;
    }
    return ans;
}

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int n, p;
        scanf("%d%d", &n, &p);
        for (int i = 0;i < n ;i++)
            scanf("%d", &R[i]);
        for (int i=0;i<n;i++)
            for (int j=0;j<p;j++)
                scanf("%d",&q[i][j]);
        for (int i = 0; i<n;i++)
            sort(q[i], q[i]+p);
        for (int i=0; i<n; i++)
            for (int j=0;j<p;j++) {
                r[i][j] = int(q[i][j] / 0.9 /R[i]+eps);
                l[i][j] = int(ceil(q[i][j] / 1.1 /R[i])+eps);
            }
        //printf("Case #%d:\n", t);
        //for (int i=0;i<n;i++)
        //    for (int j=0;j<p;j++)
        //        printf("[%d, %d]\%c", l[i][j], r[i][j], j==p-1?'\n':' ');
        //printf("%d %d\n", n, p);
        printf("Case #%d: %d\n", t, solve(n, p));
    }
    return 0;
}
