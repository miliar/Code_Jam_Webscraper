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
ld dist[105],spd[105];
ld mat[105][105];
ld dp[105][105];
int main()
{
		freopen("i.in","r",stdin);
		freopen("o.out","w",stdout);
	ll cases;
	is(cases);
	up(1,cases+1,t)
	{
		ll q; 
		
		id(n,q);
		
		up(1,n+1,i)
		{
			cin>>dist[i]>>spd[i];
		}
		
		up(1,n+1,i)
		up(1,n+1,j)
		{
			cin>>mat[i][j];
			
			dp[i][j]=1e12;
			
			if(j==i)
			mat[i][j]=0,dp[i][j]=0;
			else
			if(mat[i][j]==-1)
			mat[i][j]=1e12;
			
			
			
		}
		
		//cout<<dp[1][n]<<endl;
		up(1,n,i)
		{
			if(dist[i]>=mat[i][i+1])
			dp[i][i+1]=mat[i][i+1]/spd[i];
			//cout<<dp[i][i+1]<<endl;
			
		}
		
		up(3,n+1,k)
		up(1,n+1,i)
		for(j=i+1;j<=i+k-1 and i+k-1<=n;j++)
		{			
		
		
			if(mat[i][i+k-1]>mat[i][j]+mat[j][i+k-1])
			mat[i][i+k-1]=mat[i][j]+mat[j][i+k-1];
			//cout<<mat[i][j]<<endl;
			//cout<<dp[i][j]<<endl;
			
			//cout<<dp[1][n]<<endl;
			if(dist[i]>=mat[i][i+k-1])
			if(dp[i][i+k-1]>mat[i][i+k-1]/spd[i])
			dp[i][i+k-1]=mat[i][i+k-1]/spd[i];
			
			
			
			if(dp[i][i+k-1]>dp[i][j]+dp[j][i+k-1])
			dp[i][i+k-1]=dp[i][j]+dp[j][i+k-1];
			//cout<<dp[1][n]<<endl;
		}
		
		cin>>x>>y;
	
		cout<<"Case #"<<t<<": "<<fixed<<setprecision(6)<<dp[1][n]<<endl;
	}
}



