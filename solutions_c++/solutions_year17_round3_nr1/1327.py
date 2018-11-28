#include <bits/stdc++.h>

using namespace std;

const double pi=3.14159265359;
#define fi "testA.inp"
#define fo "testA.out"

const int maxn=1e3+7;

struct data
{
    double x;
    int y;
}a[maxn];

bool cmp(data a, data b)
{
    return a.y<b.y;
}

double f[maxn][maxn];

int main()
{
    freopen(fi,"r",stdin);
    freopen(fo,"w",stdout);
    int T;
    cin >> T;
    int test=0;
    while (T--)
    {
        test++;
        int n,k;
        cin >> n >> k;
        for (int i=1; i<=n; ++i)
        {
            long long R,H;
            scanf("%lld%lld",&R,&H);
            a[i].x=pi*2*R*H;
            a[i].y=R;
        }
        sort(a+1,a+n+1,cmp);
        memset(f,0,sizeof f);
        double res=0;
        for (int i=1; i<=n; ++i)
            for (int j=1; j<=min(i,k); ++j)
            {
                f[i][j]=max(f[i-1][j-1]+a[i].x+(pi*a[i].y*a[i].y*(j==k)),f[i-1][j]);
                if (j==k) res=max(res,f[i][j]);
            }
        printf("Case #%d: %.6f\n",test,res);
    }
}
