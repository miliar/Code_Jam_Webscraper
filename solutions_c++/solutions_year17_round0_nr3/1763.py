#include<bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define pf push_front
#define vi vector<int>
#define vl vector<ll>
#define vii vector<pii >
#define vll vector<pll>
#define pll pair<ll,ll>
#define pii pair<int,int>
#define pi 3.14159265358979
#define EL printf("\n")
#define OK printf("OK");
#define foreach(i,t) for(auto i =t.begin();i!=t.end();i++) 
#define pii pair<int,int>
#define pdn(n) printf("%d\n",n)
#define sl(n) scanf("%lld",&n)
#define sd(n) scanf("%d",&n)
#define pn printf("\n")
#define  omap unordered_map
#define PI 3.14159265
#define Inf 1e9
#define mod 1000000007
#define precise(n,k) fixed<<setprecision(k)<<n
#define fequal(a,b) (fabs(a - b)<(1e-9))
typedef long long ll;
typedef long double lf;

ll gcd(ll a,ll b){return (b==0)? a:gcd(b,a%b); }
void nope(int dec = 0){if(!dec) cout<<"NO";else cout<<"YES";exit(0);}

#define item map<ll,ll,greater<ll> >
map<ll, item > dp;
item solve(ll n,ll level)
{	
	if(dp.count(n))
		return dp[n];
	if(level==0)
	{
		item ret;
		ret[n]=1;
		return ret;
	}	

	item left,right;
	if(n%2==1)
		right=left=solve((n-1)/2,level-1);

	else
	{
		left=solve(n/2,level-1);
		right=solve(n/2-1,level-1);
	}

	item ret;
	for(auto elem:left)
		ret[elem.fi]+=elem.se;
	for(auto elem:right)
		ret[elem.fi]+=elem.se;
	return dp[n]=ret;
}
int main()
{
	std::ios::sync_with_stdio(false);cin.tie(0);
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int p=1;p<=t;p++)
	{
		ll n,k;
		cin>>n>>k;
		ll val=1,level=0;
		while(k>val)
		{
			k-=val;
			val*=2;
			level++;
		}
		dp.clear();
		item ans=solve(n,level);
		for(auto elem:ans)
		{
			if(k<=elem.se)
				{
					val=elem.fi;
					break;
				}
			k-=elem.se;
		}
		val--;
		cout<<"Case #"<<p<<": "<<(val-val/2)<<" "<<val/2<<endl;

	}
	return 0;
}