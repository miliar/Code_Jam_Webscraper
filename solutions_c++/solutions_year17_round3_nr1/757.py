#include<bits/stdc++.h>
using namespace std;
const long double PI=acos(-1);
typedef pair<long double,long double> P;
long double dp[1010][1010];
P cake[1010];
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int N,K,tcase,kase=0;
	cin>>tcase;
	while(tcase--){
		cin>>N>>K;
		memset(dp,0,sizeof dp);
		for(int i=0;i<N;i++){
			cin>>cake[i].first>>cake[i].second;
		}
		sort(cake,cake+N,greater<P>());
		for(int i=0;i<N;i++){
			dp[i][1]=cake[i].first*cake[i].first*PI+2.0*cake[i].first*cake[i].second*PI;
			if(i) dp[i][1]=max(dp[i-1][1],dp[i][1]);
			for(int j=2;j<=min(K,i+1);j++){
				dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+2.0*cake[i].first*cake[i].second*PI);
			}
		}
		cout<<setprecision(9)<<fixed<<"Case #"<<++kase<<": "<<dp[N-1][K]<<'\n';
	}
	return 0;
}
