#include <bits/stdc++.h>
using namespace std;
int T;
pair<long long,long long> a[10001];
multiset<long double> s;
int k;
long double getBest()
{
    multiset<long double>::iterator it=s.end();
    long double ret=0;
    for (int i=1;i<k;i++)
    {
        it--;
        ret+=*it;
    }
    return ret;
}
int main()
{

    freopen("in","r",stdin);
    freopen("out","w",stdout);

    scanf("%d",&T);
    for (int tt=1;tt<=T;tt++)
    {
        int n;
        scanf("%d%d",&n,&k);
        for (int i=1;i<=n;i++)
        {
            scanf("%lld%lld",&a[i].first,&a[i].second);
            a[i].second=-a[i].second;
            a[i].first=-a[i].first;
        }
        sort(a+1,a+n+1);
        long double ans=0;
        s.clear();
        for (int i=n;i>=1;i--)
        {
            if (s.size()>=k-1)
                ans=max(ans,(a[i].second)*a[i].first*2*M_PI+a[i].first*a[i].first*M_PI+getBest());
            s.insert((a[i].second)*a[i].first*2*M_PI);
        }
        printf("Case #%d: ",tt);
        cout<<setprecision(10)<<fixed<<ans<<endl;
    }
}
