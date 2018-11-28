#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
typedef pair<int,P> P1;
typedef pair<P,P> P2;
#define pu push
#define pb push_back
#define mp make_pair
#define eps 1e-7
#define INF 1000000000
#define fi first
#define sc second
#define rep(i,x) for(int i=0;i<x;i++)
#define SORT(x) sort(x.begin(),x.end())
#define ERASE(x) x.erase(unique(x.begin(),x.end()),x.end())
#define POSL(x,v) (lower_bound(x.begin(),x.end(),v)-x.begin())
#define POSU(x,v) (upper_bound(x.begin(),x.end(),v)-x.begin())
int dp[105][105][105][105];
int t,n,p,x[105],a,b,c,d;
int rec(int x,int y,int z,int w){
	if(dp[x][y][z][w]) return dp[x][y][z][w];
	if(x==a&&y==b&&z==c&&w==d) return 0;
	int S = (y+2*z+3*w)%p; if(S==0) S = 1; else S = 0;
	if(x!=a){
		dp[x][y][z][w] = max(dp[x][y][z][w],rec(x+1,y,z,w)+S);
	}
	else{
		if(y!=b) dp[x][y][z][w] = max(dp[x][y][z][w],rec(x,y+1,z,w)+S);
		if(z!=c) dp[x][y][z][w] = max(dp[x][y][z][w],rec(x,y,z+1,w)+S);
		if(w!=d) dp[x][y][z][w] = max(dp[x][y][z][w],rec(x,y,z,w+1)+S);
	}
	return dp[x][y][z][w];
}
int main(){
	cin >> t;
	for(int q=1;q<=t;q++){
		memset(dp,0,sizeof(dp));
		cin >> n >> p;
		a=0,b=0,c=0,d=0;
		for(int i=1;i<=n;i++){
			cin >> x[i];
			if(x[i]%p == 0) a++;
			if(x[i]%p == 1) b++;
			if(x[i]%p == 2) c++;
			if(x[i]%p == 3) d++;
		}
		printf("Case #%d: %d\n",q,rec(0,0,0,0));
	}
}