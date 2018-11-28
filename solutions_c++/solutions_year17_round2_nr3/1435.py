#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define sd(x) scanf("%d",&x)
#define sc(x) scanf("%c",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define mod 1000000007
#define pb push_back
#define vint vector<int>

double dp[200],en[200],sp[200],dist[200];

int main()
{
	freopen("input.txt" , "r", stdin);
	freopen("output.txt", "w", stdout);
	ll n,q,t,x,i,j,k,l;
	double timeTaken,y,z;
	slld(t);
	for(x=1;x<=t;x++){
		slld(n);slld(q);
		for(i=1;i<=n;i++){
			scanf("%lf",&en[i]);
			scanf("%lf",&sp[i]);
		}
		dist[1]=0;
		dist[0]=0;
		for(i=1;i<=n;i++){
			for(j=1;j<=n;j++){
				slld(k);
				if(j==i+1)
					dist[j]=k;
			}
			dist[i]+=dist[i-1];
		}
		while(q--){
			slld(i);
			slld(i);
		}
		dp[1]=0;
		for(i=2;i<=n;i++){
			dp[i]=10e13;
			for(j=1;j<i;j++){
				if(en[j]>=(dist[i]-dist[j]))
					dp[i]=min(dp[i],dp[j]+(dist[i]-dist[j])/sp[j]);
			}
		}
		printf("Case #%lld: %0.10lf\n",x,dp[n]);
	}
	return 0;
}