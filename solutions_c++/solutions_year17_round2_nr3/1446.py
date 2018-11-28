#include<bits/stdc++.h>
#define mod 1000000007
#define pp pair<ll,ll>
#define mp make_pair
#define ll long long
#define pb push_back
#define ff first
#define ss second
using namespace std;

ll tc,q,n,dist[110][110],s,d;
double dp[110];
pp hrse[110];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ios::sync_with_stdio(0);
	
	cin>>tc;
	for(ll t=1;t<=tc;t++){
		cin>>n>>q;
		for(ll i=1;i<=n;i++)
			cin>>hrse[i].ff>>hrse[i].ss;
		for(ll i=1;i<=n;i++){
			for(ll j=1;j<=n;j++)
				cin>>dist[i][j];
		}
		dp[n] = 0;
		for(ll i=n-1;i>0;i--){
			ll sum = 0;
			double tme=0,mn = pow(10,12);
			for(ll j=i+1;j<=n;j++){
				sum += dist[j-1][j];
				tme += (dist[j-1][j]*1.0)/hrse[i].ss;
				if(sum > hrse[i].ff)
					break;
				mn = min(tme+dp[j],mn);
			}
			dp[i] = mn;
		}
		while(q--){
			ll a,b;
			cin>>a>>b;
		}
		cout<<"Case #"<<t<<": "<<fixed<<dp[1]<<"\n";
	}
	return 0;
}

