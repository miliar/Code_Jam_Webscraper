#include<bits/stdc++.h>
#define up(j,k,i) for(i=j;i<k;i++)
#define down(j,k,i) for(i=j;i>k;i--)
#define M 1000000007
#define pp(n) printf("%lld\n",ll(n))
#define ps(n) printf("%lld ",ll(n))
#define pd(x,y) printf("%lld %lld\n",ll(x),ll(y))
#define is(n) scanf("%lld",&n)
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
pair<ld,ld> a[1005];
bool comp(ld x,ld y)
{
	return x>y;
}
bool comp1(pair<ld,ld> A, pair<ld,ld> B)
{
	return A.F>B.F;
}
int main()
{
		freopen("i.in","r",stdin);
		freopen("o.out","w",stdout);
	ll cases;
	is(cases);
	up(1,cases+1,t)
	{
	
		id(n,k);
		
		up(0,n,i)
		{
			cin>>a[i].F>>a[i].S;
		}
		
		sort(a,a+n,comp1);
		
		ld maxm=0;
		
		for(i=0;i+k-1<n;i++)
		{
			ld r=a[i].F, h=a[i].S;
		
			ld temp=acos(-1)*r*r+2*acos(-1)*r*h;
		
			vector<ld> v;
			
			up(i+1,n,j)
			{
					ld r=a[j].F, h=a[j].S;
			
				v.pb(2*acos(-1)*r*h);
			}
			
			sort(v.begin(),v.end(),comp);
			
			up(0,k-1,j)
			temp+=v[j];
			
			maxm=max(temp,maxm);
			
		}
	
	
	
	
	
	
	
	
	
	
	cout<<"Case #"<<t<<": "<<fixed<<setprecision(9)<<maxm<<endl;
	}
}

