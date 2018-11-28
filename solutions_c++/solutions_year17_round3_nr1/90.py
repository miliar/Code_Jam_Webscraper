#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N=1e3+1;
const double pi=acos(-1);
pair<ll,ll>p[N];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,T;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        int n,k,i;
        cin>>n>>k;
        for(i=0;i<n;i++)
        {
            ll x,y;
            scanf("%lld%lld",&x,&y);
            p[i]=make_pair(2.0*x*y,x);
        }
        sort(p,p+n);
        ll ans,sum=0,m=0;
        for(i=0;i<k;i++)
        {
            sum+=p[n-1-i].first;
            m=max(p[n-1-i].second,m);
        }
        ans=sum+m*m;sum-=p[n-k].first;
        for(;i<n;i++)
            ans=max(ans,sum+p[n-1-i].first+p[n-1-i].second*p[n-1-i].second);
        printf("%.10f\n",ans*pi);
    }
	return 0;
}
