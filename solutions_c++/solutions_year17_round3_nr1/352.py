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
const LL INF=1e17;
const int MOD=1e9+7;
const double PI=acos(-1);
// >.<
int t,tc=1,n,k;
pair<LL,LL> pancake[1000];
LL dp[1000][1001];
bool vis[1000][1001];
LL f(int x,int y){
	if(x>=n)return (y==0)?0:-INF;
	if(y<0)return -INF;
	if(vis[x][y])return dp[x][y];
	LL ret=f(x+1,y);
	LL a1=pancake[x].FI*pancake[x].SE*2;
	LL a2=pancake[x].FI*pancake[x].FI;
	if(y==k)ret=max(ret,f(x+1,y-1)+a1+a2);
	else ret=max(ret,f(x+1,y-1)+a1);
	vis[x][y]=1;
	return dp[x][y]=ret;
}
bool cmp(pair<LL,LL> &x,pair<LL,LL> &y){
	return (x.FI>y.FI);
}
int main(){
	scanf("%d",&t);
	while(t--){
		scanf("%d %d",&n,&k);
		REP(i,n)scanf("%lld %lld",&pancake[i].FI,&pancake[i].SE);
		sort(pancake,pancake+n,cmp);
		RESET(vis,0);
		LL an=f(0,k);
		printf("Case #%d: %.9lf\n",tc++,(double)an*PI);
	}
	return 0;
}