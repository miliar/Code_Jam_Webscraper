#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> PI;
const double eps=1e-6;
const int mod=1e9+7;
const double pi=acos(-1.0);
const int N=1e5+5;
const int M=100;

struct node
{
    LL r, h;
}a[1005], b[1005];

bool cmp1(node a, node b)
{
    return 2*pi*a.r*a.h>2*pi*b.r*b.h;
}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, ca=1;
    scanf("%d", &t);
    while(t--)
    {
        printf("Case #%d: ", ca++);
        int n, k;
        scanf("%d%d", &n, &k);
        for(int i=0;i<n;i++)
        {
            cin>>a[i].r>>a[i].h;
        }
        if(k==0)
        {
            puts("0.000000000");
            continue;
        }
        double maxn=0;
        for(int i=0;i<n;i++)
        {
            memset(b, 0, sizeof(b));
            double ans=pi*a[i].r*a[i].r+2.0*pi*a[i].r*a[i].h;
            int d=0;
            for(int j=0;j<n;j++)
                if(i!=j)
                    b[d++]=a[j];
            sort(b, b+d, cmp1);
            for(int j=0;j<k-1;j++)
                ans+=2.0*pi*b[j].r*b[j].h;
            maxn=max(maxn, ans);
        }
        printf("%.9f\n", maxn);
    }
    return 0;
}
