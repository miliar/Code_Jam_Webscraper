#include<bits/stdc++.h>
using namespace std;
#define REP(_x,_y) for(int (_x)=0;(_x)<(_y);(_x)++)
#define FOR(_x,_y,_z) for(int (_x)=(_y);(_x)<=(_z);(_x)++)
#define FORD(_x,_y,_z) for(int (_x)=(_y);(_x)>=(_z);(_x)--)
#define RESET(_x,_y) memset((_x),(_y),sizeof(_x))
#define SZ(_x) ((int)(_x).size())
#define LEN(_x) strlen(_x)
#define ALL(_x) (_x).begin(),(_x).end()
#define LL long long
#define ULL unsigned LL
#define PII pair<int,int>
#define VI vector<int>
#define VII vector< PII >
#define VVI vector< VI >
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
const int INF=1e9;
const int MOD=1e9+7;
// >.<
int t,tc=1,n,q,from,to;
double e[100],s[100],d[100][100];
// small
double dp[100];
bool vis[100];
double f(int x){
	if(x==n-1)return 0.0;
	if(vis[x])return dp[x];
	double ret=1e15,dist=0.0;
	FOR(i,x+1,n-1){
		dist=dist+d[i-1][i];
		if(dist>e[x])break;
		ret=min(ret,f(i)+dist/s[x]);
	}
	vis[x]=1;
	return dp[x]=ret;
}
void solve_small(){
	RESET(vis,0);
	double an=f(0);
	printf("Case #%d: %.7lf\n",tc++,an);
}
int main(){
	scanf("%d",&t);
	while(t--){
		scanf("%d %d",&n,&q);
		REP(i,n)scanf("%lf %lf",&e[i],&s[i]);
		REP(i,n)REP(j,n)scanf("%lf",&d[i][j]);
		while(q--){
			scanf("%d %d",&from,&to);
			solve_small();
		}
	}
	return 0;
}