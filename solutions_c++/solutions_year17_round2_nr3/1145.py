/*input
1
10 1
12664 191
15592 947
5520 280
14539 466
6693 324
18598 684
17228 160
11984 130
7864 1000
20000 1000
-1 9054 -1 -1 -1 -1 -1 -1 -1 -1
-1 -1 3979 -1 -1 -1 -1 -1 -1 -1
-1 -1 -1 2196 -1 -1 -1 -1 -1 -1
-1 -1 -1 -1 826 -1 -1 -1 -1 -1
-1 -1 -1 -1 -1 5638 -1 -1 -1 -1
-1 -1 -1 -1 -1 -1 7955 -1 -1 -1
-1 -1 -1 -1 -1 -1 -1 1379 -1 -1
-1 -1 -1 -1 -1 -1 -1 -1 243 -1
-1 -1 -1 -1 -1 -1 -1 -1 -1 1054
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1
*/
#include <bits/stdc++.h>
using namespace std;
pair<long double,long double> a[105];
long double memo[105][105];
long double d[105][105],dist[105];
long long int n;
long double dfs(int k,int h){
	if(k==n-1) return 0;
	if(memo[k][h]!=-1) return memo[k][h];
	long double ans1=(dist[k+1]-dist[k])/a[k].second+dfs(k+1,k);
	if(dist[k+1]-dist[h]<=a[h].first&&h!=k){
		long double ans2=(dist[k+1]-dist[k])/a[h].second+dfs(k+1,h);
		memo[k][h]=min(ans1,ans2);
	}
	else memo[k][h]=ans1;
	return memo[k][h];
}
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	long long int tc=1,T;
	for(cin>>T;tc<=T;++tc,cout<<'\n'){
		cout<<"Case #"<<tc<<": ";
		long long int q;
		cin>>n>>q;
		for(int i=0;i<n;cin>>a[i].first>>a[i].second,++i);
		for(int i=0;i<n;++i)
			for(int j=0;j<n;cin>>d[i][j++]);
		dist[0]=0;
		for(int i=0;i<n;++i) dist[i+1]=dist[i]+d[i][i+1];
		//for(int i=0;i<n;cout<<dist[i++]<<" ");cout<<'\n';
		while(q--){
			long long int u,v;
			cin>>u>>v;
			for(int i=0;i<105;++i)
				for(int j=0;j<105;++j) memo[i][j]=-1;
			cout<<fixed<<setprecision(6)<<dfs(0,0);
		}
	}
}