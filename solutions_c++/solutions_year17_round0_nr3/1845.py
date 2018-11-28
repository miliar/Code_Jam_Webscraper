#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;
typedef long long int ll;

ll solve(ll N,ll K)//2k+1->k,k+1 * 2k -> k,k ‚ğ‘å‚«‚¢‚à‚Ì‚©‚çK‰ñŒJ‚è•Ô‚µ‚Äc‚è‚ÌÅ‘å
{
	if(K==0) return N;
	ll f=N,s=f+1;
	ll a=1,b=0;
	while(1)
	{
		if(K<b) return s;
		K-=b;
		if(K<a) return f;
		K-=a;
		if(f%2==0)
		{
			ll nf=f/2,ns=nf+1;
			ll na=0,nb=0;
			na+=b,nb+=b;
			na+=2LL*a;
			f=nf,s=ns,a=na,b=nb;
		}
		else
		{
			ll nf=f/2,ns=nf+1;
			ll na=0,nb=0;
			na+=a,nb+=a;
			nb+=2LL*b;
			f=nf,s=ns,a=na,b=nb;
		}
	}
	return 0LL;
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		ll N,K;
		scanf("%lld %lld",&N,&K);
		ll zan=solve(N+1,K-1)-1LL;
		//printf("%lld %lld : %lld\n",N+1,K-1,zan+1);
		printf("%lld %lld\n",zan/2LL,(zan-1LL)/2LL);
	}
	return 0;
}
