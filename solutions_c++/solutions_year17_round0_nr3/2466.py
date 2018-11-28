#include<bits/stdc++.h>
#define up(j,k,i) for(i=j;i<k;i++)
#define down(j,k,i) for(i=j;i>k;i--)
#define M 1000000007
#define pp(n) printf("%lld\n",ll(n))
#define ps(n) printf("%lld ",ll(n))
#define pd(x,y) printf("%lld %lld\n",ll(x),ll(y))
#define is(n) scanf("%lld",&n)
#define max(x,y) max(ll(x),ll(y))
#define min(x,y) min(ll(x),ll(y))
#define inf LLONG_MAX
#define id(n,m) scanf("%lld%lld",&n,&m)
#define it(n,m,k) scanf("%lld%lld%lld",&n,&m,&k)
#define ss(s) scanf("%s",s)
#define cool 0
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define pll pair<ll,ll> 
#define db cout<<"######\n"
#define null(a) memset(a,0,sizeof(a))
#define neg(a) memset(a,255,sizeof(a))
typedef long double ld;
typedef long long int ll;
using namespace std;
ll i,j,k,z,t,n,m,sum,ans,x,y,maxm=0,minm=inf; bool flag;
int main()
{
		freopen("i.in","r",stdin);
		freopen("o.out","w",stdout);
	ll cases;
	is(cases);
	up(1,cases+1,t)
	{
		map<ll,ll> p;
		priority_queue<ll> Q;
	
		id(n,k);
		
		p[n]=1;
		Q.push(n);
		ll cur=0;
		
		while(1)
		{
			x=Q.top();
			cur+=p[x];
			Q.pop();
			
			ll ml=(x-1)/2,mr=x/2;
			
			if(!p[ml])
			Q.push(ml);
			
			p[ml]+=p[x];
			
			if(!p[mr])
			Q.push(mr);
			
			p[mr]+=p[x];
			
			
			if(cur>=k)
			{
				cout<<"Case #"<<t<<": "<<mr<<" "<<ml<<endl;
				break;
			}
			
		}
	
	}
}

