#include <bits/stdc++.h>
#define mp make_pair
#define ff first
#define se second
#define pb push_back
#define nn 110
#define pii pair<int,int>
#define mt make_tuple
#define ll long long int
#define pdd pair<long double,long double>
#define db double
#define pll pair<ll,ll>
#define pli pair<ll,int>
#define inf 1000000000000010ll
#define logn 20
#define mod 1000000007
#define mt make_tuple
 
using namespace std;

pdd h[nn];
long db d[nn];
long db dp[nn];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    #endif
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
    	cout<<"Case #"<<tt<<": ";
    	int n,q;
    	cin>>n>>q;
    	memset(d,0,sizeof d);
    	for(int i=0;i<n;i++)
    		cin>>h[i].ff>>h[i].se;
    	int flag=0;
    	for(int i=0;i<n;i++)
    	{
    		for(int j=0;j<n;j++)
    		{
    			int w;
    			cin>>w;
    			if(j==i+1)
    				d[i]=w;
    		}
    	}
    	int u,v;
    	cin>>u>>v;
    	for(int i=0;i<n-1;i++)
    		dp[i]=inf;
    	dp[n-1]=0;
    	for(int i=n-2;i>=0;i--)
    	{
    		long db w=d[i];
    		for(int j=i+1;j<n && w<=h[i].ff;j++)
    		{
    			long db tmp=(w/h[i].se);
    			dp[i]=min(dp[i],tmp+dp[j]);
    			w+=d[j];
    		}
    	}
    	cout<<fixed<<setprecision(7)<<dp[0]<<endl;
    }
    return 0;
}