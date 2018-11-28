
#include <iostream>
#include <algorithm>
#include <cstdio>
const double  eps = 0.0000000001;
const double PI=acos(-1.0);
using namespace std;
struct node {
    double r,h;
    double cs,ds,s;
}a[1111];
bool cmp(node a,node b)
{
    return a.cs >b.cs;
}
int main()
{
        freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int M;
    int tes = 0;
    cin >> M;
    while (M--)
    {
    int N,k;
    cin >> N >>k;
    double ans = 0;
    for (int i = 1; i<=N; i++)
    {
        scanf("%lf%lf",&a[i].r,&a[i].h);
        a[i].cs = a[i].r*PI*2*a[i].h;
        a[i].ds =  PI * a[i].r *a[i].r;
        a[i].s = a[i].cs + a[i].ds;
    }
    sort(a+1,a+N+1,cmp);
    for (int i = 1;i<=N; i++)
        {
            double dr = a[i].r;
            double sum =PI * a[i].r *a[i].r +  a[i].r*PI*2*a[i].h;
            int cnt = 1;
            for (int j = 1; j<=N&&cnt<k; j++ )
            {
                if (i==j) continue;
                if (dr+eps>=a[j].r) {sum+=a[j].r*PI*2*a[j].h;cnt++;}
            }
            if (cnt==k) ans = max(sum,ans);
        }
    printf("Case #%d: %.12f\n",++tes,ans);
}
}
