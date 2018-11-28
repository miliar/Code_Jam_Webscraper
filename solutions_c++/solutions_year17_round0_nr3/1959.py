#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <map>
using namespace std;

#define X first
#define Y second
#define N 1010
#define M 500010

typedef long long ll;
const int INF=1ll<<30;

pair<ll,ll> Solve(ll n,ll k)
{
	ll a=0,b=n,aa,bb,c1=0,c2=1;
	while (true)
	{
		//cout<<a<<" "<<c1<<" "<<b<<" "<<c2<<" "<<k<<endl;
		if (k<=c2)
		{
			if (b&1) return make_pair(b/2,b/2);
			else return make_pair(b/2-1,b/2);
		}
		k-=c2;
		if (!c1)
		{
			if (b&1)
			{
				c2<<=1;
				b>>=1;
			}
			else
			{
				a=b/2-1;
				b>>=1;
				c1=c2;
			}	
		}
		else
		{
			if (k<=c1)
			{
				if (a&1) return make_pair(a/2,a/2);
				else return make_pair(a/2-1,a/2);
			}
			k-=c1;
			if (b&1)
			{
				a=a/2-1,b=b/2;
				c2=c2*2+c1;
			}
			else
			{
				a=a/2,b=b/2;
				c1=c1*2+c2;
			}
		}
	} 
}

int main()
{
	//freopen("in.in","r",stdin);
	//freopen("C.out","w",stdout);
	
	int T; scanf("%d",&T); ll n,k;
	for (int cas=1;cas<=T;cas++)
	{
		printf("Case #%d: ",cas);
		scanf("%I64d%I64d",&n,&k);
		pair<ll,ll> res=Solve(n,k);
		printf("%I64d %I64d\n",res.Y,res.X);
	}
	
	return 0;
}
