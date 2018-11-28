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
		is(n); ans=0;
		
		if(n/10==0)
		{
			cout<<"Case #"<<t<<": "<<n<<endl;
			continue;
		}
		
		vector<ll> v;
		
		x=n;
		
		while(x)
		{
			v.pb(x%10);
			x/=10;
		}
		
		ll tot=v.size(); ll cur=1;
		
		for(i=tot-2;i>=0;i--)
		if(v[i]<v[i+1])		
		break;
		else
		if(v[i]==v[i+1])cur++;
		else
		cur=1;
		
		if(cur==tot or i==-1)
		{
			cout<<"Case #"<<t<<": "<<n<<endl;
			continue;
		}
		
		
		
		//pd(i,cur);
		up(0,i+cur,j)
		v[j]=9;
		
		v[j]--;
		
		ll fact=1;
		
		up(0,tot,i)
		ans+=v[i]*fact,fact*=10;
		
		cout<<"Case #"<<t<<": "<<ans<<endl;
	
	}
}

