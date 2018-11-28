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
int main()
{
	freopen("in.in", "r", stdin);
	freopen("out2.txt", "w", stdout);
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		int n,r,o,y,g,b,v;
		cin>>n>>r>>o>>g>>y>>b>>v;
		bool validr=true,validb=true,validg=true;
		char first;
		string ans="";
		if(r>0)
		{
			ans+='R';
			first='r';
			r--;
			validr=false;
		}
		else if(b>o)
		{
			ans+='B';
			first='b';
			b--;
			validb=false;
		}
		else if(g>0)
		{
			ans+='Y';
			first='g';
			g--;
			validg=false;
		}
		for(int i=1;i<n;i++)
		{
			//cout<<r<<g<<b<<" "<<ans<<endl;
			if(!validr)
			{
				//cout<<1<<endl;
				if(b==g)
				{
					if(first=='g')
					{
						ans+='Y';
						g--;
						validg=false;
						validr=true;
						validb=true;
					}
					else
					{
						ans+='B';
						b--;
						validb=false;
						validg=true;
						validr=true;
					}
				}
				else if(b>g)
				{
					ans+='B';
					b--;
					validb=false;
					validg=true;
					validr=true;
				}
				else
				{
					ans+='Y';
					g--;
					validg=false;
					validr=true;
					validb=true;
				}
			}
			else if(!validb)
			{
				//cout<<2<<endl;
				if(r==g)
				{
					if(first=='g')
					{
						ans+='Y';
						g--;
						validg=false;
						validr=true;
						validb=true;
					}
					else
					{
						ans+='R';
						r--;
						validr=false;
						validg=true;
						validb=true;
					}
				}
				else if(r>g)
				{
					ans+='R';
					r--;
					validr=false;
					validg=true;
					validb=true;
				}
				else
				{
					ans+='Y';
					g--;
					validg=false;
					validr=true;
					validb=true;
				}
			}
			else if(!validg)
			{
				if(b==r)
				{
					if(first=='r')
					{
						ans+='R';
						r--;
						validr=false;
						validg=true;
						validb=true;
					}
					else
					{
						ans+='B';
						b--;
						validb=false;
						validr=true;
						validg=true;
					}
				}
				else if(b>r)
				{
					//cout<<"HERE"<<endl;
					ans+='B';
					b--;
					validb=false;
					validr=true;
					validg=true;
				}
				else
				{
					ans+='R';
					r--;
					validr=false;
					validg=true;
					validb=true;
				}
			}
		}
		//cout<<ans<<endl;
		for(int i=0;i<n;i++)
		{
			int loo=i-1;
			if(i==0)
				loo=n-1;
			if(ans[i]==ans[(i+1)%n]||ans[i]==ans[loo])
				{ans="IMPOSSIBLE";break;}
		}
		if(r!=0||b!=0||g!=0)
			ans="IMPOSSIBLE";
		cout<<"Case #"<<tt<<": "<<ans<<endl;
	}
	//cout<<t<<endl;
	return 0;
}