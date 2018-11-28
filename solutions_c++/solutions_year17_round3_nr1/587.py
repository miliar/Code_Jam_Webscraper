#include <bits/stdc++.h>
#define MAX 1000005
#define ll long long
#define upperlimit 1000100
#define INF 1e18
#define eps 1e-8
#define endl '\n'
#define pcc pair<char,char>
#define pii pair<int,int>
#define pll pair<ll,ll>
#define tr(container,it) for(typeof(container.begin()) it=container.begin();it!=container.end();it++)
#define MOD 1000000007
#define slld(t) scanf("%lld",&t)
#define sd(t) scanf("%d",&t)
#define pd(t) printf("%d\n",t)
#define plld(t) printf("%lld\n",t)
#define mp(a,b) make_pair(a,b)
#define FF first
#define SS second
#define pb(x) push_back(x)
#define vi vector<int>
#define clr(a) memset(a,0,sizeof(a))
#define debug(a) printf("check%d\n",a)
#define csl ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
using namespace std;
 
ll gcd(ll n1,ll n2){
	if(n1%n2==0)return n2;
	return gcd(n2,n1%n2);
}
ll powmod(ll base,ll exponent)
{
	ll ans=1;
	while(exponent){
		if(exponent&1)ans=(ans*base)%MOD;
		base=(base*base)%MOD;
		exponent/=2;
	}
	return ans;
}
pair <double,double > cake[MAX];
set <pair<double,int> > s;
int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		s.clear();
		int n,k;
		cin>>n>>k;
		for(int i=1;i<=n;i++)
		{
			cin>>cake[i].FF>>cake[i].SS;
		}
		double sum=0.0,ans=0.0;
		sort(cake+1,cake+n+1);
		for(int i=1;i<=k-1;i++)
		{
			sum+=2.0*cake[i].FF*cake[i].SS;
			s.insert(mp(2.0*cake[i].FF*cake[i].SS,i));
		}

		for(int i=k;i<=n;i++)
		{
			double now=cake[i].FF*cake[i].FF+2.0*cake[i].FF*cake[i].SS+sum;
			ans=max(now,ans);
			if(s.size()>0&&s.begin()->FF<2.0*cake[i].FF*cake[i].SS)
			{
				sum-=s.begin()->FF;
				s.erase(s.begin());
				sum+=2.0*cake[i].FF*cake[i].SS;
				s.insert(mp(2.0*cake[i].FF*cake[i].SS,i));
			}
		}
		cout<<"Case #"<<tt<<": ";
		ans=3.14159265359*ans;
		printf("%0.9llf\n",ans);
	}
	//cout<<t<<endl;
	return 0;
}