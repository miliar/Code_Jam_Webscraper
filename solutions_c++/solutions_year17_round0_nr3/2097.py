#include<bits/stdc++.h>
#define pi pair<long long, long long>
#define mp make_pair
#define fi first
#define se second
using namespace std;
typedef long long ll;
ll n,k;
pi calc(ll x)
{
    ll l=(x+1)/2-1,r=x-(x+1)/2;
    return mp(l,r);
}

ll get()
{
    ll a=n,b=n,ca=1,cb=0;
    while (k>0)
	{
		pi sa=calc(a),sb=calc(b);
		ll ta,tb,tca=0,tcb=0;
		k-=ca; if (k<=0) return a;
		k-=cb; if (k<=0) return b;
		ta=max(max(sa.fi,sa.se),max(sb.fi,sb.se));
		tb=min(min(sa.fi,sa.se),min(sb.fi,sb.se));
		if (ta==tb)
		{
			a=b=ta=tb;
			ca=2*(ca+cb);
			cb=0;
		}
		else {
			if (sa.fi==ta) tca+=ca; else tcb+=ca;
			if (sa.se==ta) tca+=ca;	else tcb+=ca;
			if (sb.fi==ta) tca+=cb;	else tcb+=cb;
			if (sb.se==ta) tca+=cb;	else tcb+=cb;
			a=ta; ca=tca;
			b=tb; cb=tcb;
		}
	}
	return a;
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("c.out","w",stdout);
    int cas;
    scanf("%d",&cas);
    for (int tt=1; tt<=cas; tt++)
    {
        scanf("%lld%lld",&n,&k);
        printf("Case #%d: ",tt);
        ll m=get();
        pi p=calc(m);
        printf("%lld %lld\n",max(p.fi,p.se),min(p.fi,p.se));
    }
}
