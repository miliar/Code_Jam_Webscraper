#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define sci(fd) scanf("%d",&fd)
#define scll(fd) scanf("%lld",&fd)
#define pb push_back
#define mp make_pair
#define MOD 1000000007
#define PI 3.1415926535897932
#define pii pair < int,int > 
#define pll pair < ll,ll >
#define fi first
#define se second
#define LOGN 20
const ll infi=1000000000000000009;
vector < pll > v;
int main()
{
    int t;
    sci(t);
    ll y=0;
    while(t--)
    {
        v.clear();
        ll i,j,n,d,a,b,a1,b1,a2,b2;
        scll(d);
        scll(n);
        for(i=0;i<n;i++)
        {
            scll(a);
            scll(b);
            v.pb(mp(a,b));
        }
        sort(v.begin(), v.end());
        double ans=10000000000000000000000.0;
        //printf("%0.6lf\n",ans);
        for(i=0;i<n;i++)
        {
            double yy=d;
            for(j=i+1;j<n;j++)
            {
                b1=v[i].se;
                b2=v[j].se;
                if(b1<=b2)
                continue;
                double tt=(v[j].fi-v[i].fi)/((b1-b2)*1.0);
                double dd=v[i].fi+b1*tt;
                if(dd<yy)
                dd=yy;
            }
            yy=yy-v[i].fi;
            //printf("%0.6lf\n",yy);
            double ss=(d*v[i].se)/(yy*1.0);
            if(ss<ans)
            ans=ss;
        }
        y++;
        printf("Case #%lld: %0.6lf\n",y,ans);
    }
    return 0;
}