#include <bits/stdc++.h>
using namespace std;

#define sd(x) scanf("%d",&x)
#define su(x) scanf("%u",&x)
#define slld(x) scanf("%lld",&x)
#define sc(x) scanf("%c",&x)
#define ss(x) scanf("%s",x)
#define sf(x) scanf("%f",&x)
#define slf(x) scanf("%lf",&x)
#define ll long long int
#define mod(x,n) (x+n)%n

map<ll,ll> Count;
set<ll> S;

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);

	ll i,j,k,l,m,n,t,tno,x,y,z;

	slld(t);	tno=1;
	while(tno<=t)
	{
		slld(n);	slld(k);

		Count.clear();	S.clear();
		S.insert(n);	Count[n]=1;		x=0;
		set<ll>::iterator it;

		while(x<k)
		{
			it = S.end();	it--;
			y = *it;

			x+=Count[y];
			S.erase(y);

			if(y%2==0)
			{
				S.insert(y/2-1);
				Count[y/2-1]+=Count[y];
				S.insert(y/2);
				Count[y/2]+=Count[y];				
			}
			else
			{
				S.insert(y/2);
				Count[y/2]+=2*Count[y];
			}

		}	

		if(y%2==0)
		{	z=y/2-1;	y=y/2;	}
		else	
		{	z=y=y/2;	}	

		printf("Case #%lld: %lld %lld\n", tno, y, z );
		tno++;
	}	
	
	return 0;
}