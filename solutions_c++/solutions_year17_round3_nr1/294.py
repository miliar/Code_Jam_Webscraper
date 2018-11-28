#include<stdio.h>
#include<algorithm>
#include<math.h>
using namespace std;
#define PI (3.141592653589793238)
struct Cake
{
    long long rad;
    long long hei;
    double suf;
    bool operator()(Cake a, Cake b)
    {
        if(a.suf==b.suf) return a.hei>b.hei;
        return a.suf>b.suf;
    }
}arr[1010];
long long n, k;
double ans;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    long long tt, T;
    int i;
    scanf("%lld", &T);
    for(tt=1; tt<=T; ++tt)
    {
        scanf("%lld%lld", &n, &k);
        ans=0;
        for(i=1; i<=n; ++i)
        {
            scanf("%lld%lld", &arr[i].rad, &arr[i].hei);
            arr[i].suf = (double)2*arr[i].rad*arr[i].hei;
        }
        long long p, m=-1, q;
        sort(&arr[1], &arr[n+1], Cake());
        for(i=1; i<=n; ++i)
        {
            if(arr[i].rad > m){
                m = arr[i].rad;
                p=i;
            }
        }
        ans = m*m + arr[p].suf; q=0;
        for(i=1; i<k; ++i)
        {
            ++q;
            if(q==p) ++q;
            ans += arr[q].suf;
        }
        double ans2=0;
        m=-1;
        for(i=1; i<=k; ++i)
        {
            ans2 += arr[i].suf;
            if(m < arr[i].rad) m = arr[i].rad;
        }
        ans2 += m*m;
        //printf("%f %f\n", ans, ans2);
        if(ans>ans2) printf("Case #%lld: %.9f\n", tt, ans*PI);
        else printf("Case #%lld: %.9f\n", tt, ans2*PI);
    }
}
