#include <bits/stdc++.h>
#define MAXX 1000005
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
int l[1005],r[1005];
int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		int n,k;
		cin>>n>>k;
		for(int i=1;i<=n;i++)
			l[i]=i-1;
		for(int j=1;j<=n;j++)
			r[j]=n-j;
		int maxi=-1;
		for(int i=1;i<=k;i++)
		{
			maxi=-1;
			for(int j=1;j<=n;j++)
			{
				int mm=min(l[j],r[j]);
				if(min(l[maxi],r[maxi])<mm)
				{
					maxi=j;
				}
				if(min(l[maxi],r[maxi])==mm)
				{
					if(max(l[maxi],r[maxi])<=mm)
					maxi=j;					
				}
			}
			//cout<<maxi<<endl;
			if(i==k)
				continue;
			for(int i=1;i<=maxi;i++)
				r[i]=min(maxi-i-1,r[i]);
			for(int j=maxi;j<=n;j++)
				l[j]=min(j-maxi-1,l[j]);
		}
		cout<<"Case #"<<tt<<": "<<max(l[maxi],r[maxi])<<" "<<min(l[maxi],r[maxi])<<endl;
	}
	return 0;
}