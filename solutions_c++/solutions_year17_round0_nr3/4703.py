#include<bits/stdc++.h>
using namespace std;

#define sd(mark) scanf("%d",&mark)
#define ss(mark) scanf("%s",mark)
#define sl(mark) scanf("%lld",&mark)
#define debug(mark) printf("check%d\n",mark)
#define clr(mark) memset(mark,0,sizeof(mark))
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define ll long long

map<ll,ll> freq;
int main()
{
	// freopen ("C2.in","r",stdin);
	// freopen ("C2.out","w",stdout);
	int t;
	sd(t);
	for(int tt=1;tt<=t;tt++)
	{
		ll n,k;
		freq.clear();
		sl(n);sl(k);
		freq[-n]=1;
		while(true)
		{
			map<ll,ll>::iterator it=freq.begin();
			ll val=-it->F-1;
			ll f=it->S;
			if(it->S>=k)	break;
			k-=(it->S);
			freq.erase(it);
			freq[-(val/2)]+=f;
			freq[-val+val/2]+=f;
		}
		ll val=-(freq.begin())->F-1;
		printf("Case #%d: %lld %lld\n",tt,max(val/2,val-val/2),min(val/2,val-val/2));
	}
}