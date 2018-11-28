#include <bits/stdc++.h>
 
using namespace std;
#define go_baby_go ios::sync_with_stdio(false);cin.tie(NULL);
#define pb push_back
#define pp pop_back
#define f first
#define s second
#define mp make_pair
#define ll long long
const int size=1e3+7;
#define pi 3.1415926535897
pair<ll,ll> a[size];
ll dp[size][size];

ll rec(int n,int k)
{
	if(dp[n][k])return dp[n][k];
	if(n<k)return -1;
	if(k==1)return dp[n][1]=2*a[n].s*1ll*a[n].f;
	
	ll sum=2*a[n].f*a[n].s,val=0;
	for(int i=n-1;i>0;i--)
	{
		val=max(val,rec(i,k-1));
	}
	dp[n][k]=val;
	//cerr<<n<<" "<<k<<" "<<val<<endl;
	if(val==-1)return -1;
	else return dp[n][k]+=sum;
}
void solve()
{
	int n,k,x,y;
	cin>>n>>k;

	for(int i=1;i<=n;i++)
	{	cin>>x>>y;
		a[i]=make_pair(x,y);
		
	}
	sort(a+1,a+n+1);
	for(int i=1;i<=n;i++)
	for(int j=1;j<=n;j++)
		dp[i][j]=0;
	for(int i=n;i>0;i--)
	{
		dp[i][k]=rec(i,k);
		if(dp[i][k]>0)dp[i][k]+=a[i].f*a[i].f;
	}
	//cerr<<",,,,,,,\n";
	ll ans=0;
	for(int i=1;i<=n;i++)
		{
			ans=max(ans,dp[i][k]);}
		//	cerr<<dp[i][k]<<" ";}cerr<<endl;
	double val=ans*1.0*pi;
	cout<<val<<endl;
}
int main()
{
	go_baby_go
	int t,T;
	cin>>t;
	T=t;
	cout<<setprecision(8);
	cout<<fixed;
	while(t--)
	{
		cout<<"Case #"<<T-t<<": ";
		solve();
	}
	return 0;
}

