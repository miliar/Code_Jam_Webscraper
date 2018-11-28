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
pii a[MAX];
pii b[MAX];
int x[MAX];
set<pii> s;
int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{

        for(int i=0;i<=1440;i++)x[i]=0;
		int n,k,ans=0;
		cin>>n>>k;
		int  sum1=0,sum2=0;
		for(int i=0;i<n;i++)
		{
			cin>>a[i].FF>>a[i].SS;
			sum1+=a[i].SS-a[i].FF;
		}
		sort(a,a+n);
		for(int i=0;i<k;i++)
		{
			cin>>b[i].FF>>b[i].SS;
			sum2+=b[i].SS-b[i].FF;
			x[b[i].FF]=1;
		}
		sort(b,b+k);
		for(int i=1;i<n;i++)
		{
			bool bl=true;
			for(int j=a[i-1].SS;j<=a[i].FF;j++)
			{
				if(x[j]==1)bl=false;
			}
			if(bl)s.insert(mp(a[i].FF-a[i-1].SS,i));
		}
		bool bl=true;

		for(int i=a[n-1].SS;i<=1440;i++){if(x[i]==1)bl=false;}
			for(int i=0;i<=a[0].FF;i++){if(x[i]==1)bl=false;}
				//cout<<bl<<endl;
				int h=1440-a[n-1].SS+a[0].FF;
				h=max(h,0);
				if(bl)s.insert(mp(h,0));
		while(!s.empty())
		{
			int h=s.begin()->FF;
			//cout<<h<<" vv "<<s.begin()->SS<<" "<<sum1<<endl;
			if(sum1+h<=720){sum1+=h;ans++;}
			s.erase(s.begin());
		}
        int ans1=2*n-2*ans;
        ans=0;
        for(int i=0;i<=1440;i++)x[i]=0;
        for(int i=0;i<n;i++)x[a[i].FF]=1;
        for(int i=1;i<k;i++)
		{
			bool bl=true;
			for(int j=b[i-1].SS;j<=b[i].FF;j++)
			{
				if(x[j]==1)bl=false;
			}
			if(bl)s.insert(mp(b[i].FF-b[i-1].SS,i));
		}
		 bl=true;

		for(int i=b[k-1].SS;i<=1440;i++){if(x[i]==1)bl=false;}
			for(int i=0;i<=b[0].FF;i++){if(x[i]==1)bl=false;}
			 h=1440-b[k-1].SS+b[0].FF;
				h=max(h,0);
				if(bl)s.insert(mp(h,0));
				ans=0;
		while(!s.empty())
		{
			int h=s.begin()->FF;
			//cout<<h<<" "<<s.begin()->SS<<" "<<sum2<<endl;
			if(sum2+h<=720){sum2+=h;ans++;}
			s.erase(s.begin());
		}
        ans1=max(ans1,2*k-2*ans);
		cout<<"Case #"<<tt<<": "<<ans1<<endl;
		//ans=3.14159265359*ans;
		//printf("%0.9llf\n",ans);
	}
	//cout<<t<<endl;
	return 0;
}