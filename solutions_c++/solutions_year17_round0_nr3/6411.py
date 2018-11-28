#include<bits/stdc++.h>
#define	    ll		    long long int
#define     D               double
#define     LD              long double
#define     max(a,b)	    ((a)>(b)?(a):(b))
#define     min(a,b)	    ((a)<(b)?(a):(b))
#define     mp              make_pair
#define     vi              vector<ll>
#define     pb              push_back
#define     s               second
#define     f               first
#define     mod             1000000007
using namespace std;
inline ll getn(){
	ll n=0, c=getchar();
	while(c < '0' || c > '9')
		c = getchar();
	while(c >= '0' && c <= '9')
		n = (n<<3) + (n<<1) + c - '0', c = getchar();
	return n;
}


int main()
{
	//	std::ios_base::sync_with_stdio(0);
	ll t,n,j,i,p,k,l,ji,a,b;
	FILE *wfile;
	
	cin>>t;
//	string str,str1;
	wfile=fopen("output1.txt","w");
	ji=0;
	string str,str1;
	ll dp[1005];
	ll arr[1005];
while(t--)
{
	priority_queue<ll> qi;
	ji++;
	cin>>a>>b;
	ll ans=0;
	n=str.size();
	memset(dp,0,sizeof(dp));
	memset(arr,0,sizeof(arr));
	map<ll,ll> mp;
	qi.push(a);
	mp[a]+=1;
	ll ans1=0;
	ll ans2=0;
	//cout<<ji<<endl;
	while(b>0)
	{
		p=qi.top();
		l=mp[p];
		qi.pop();
	//	cout<<p<<" "<<l<<endl;
		ll x;
		ll y;
		if(p%2)
		{
			x=p/2;
			y=x;
		}
		else
		{
			y=p/2;
			x=y-1;

		}
		if(l>=b)
		{
			ans1=y;
			ans2=x;
			break;
		}
		else
		{

			b-=l;
			if(mp[x]==0)
			{
				qi.push(x);
			}
			mp[x]+=l;
			if(mp[y]==0)
			{
				qi.push(y);
			}
			mp[y]+=l;
		}
	}
	//cout<<endl;
	fprintf(wfile,"Case #%lld: ",ji);
	
fprintf(wfile,"%lld %lld",ans1,ans2);
	fprintf(wfile,"\n");
}
	
	return 0;
}
