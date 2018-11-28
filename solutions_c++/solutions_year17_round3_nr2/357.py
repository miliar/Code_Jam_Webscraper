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
int t,tc=1,ac,aj,dp[24*60][721][2],beginning;
bool c_is_busy[24*60],j_is_busy[24*60];
int f(int x,int y,int z){
	if(x==24*60){
		if(y==0){
			if(z==beginning)return 0;
			return 1;
		}
		return INF;
	}
	if(y<0)return INF;
	if(dp[x][y][z]!=-1)return dp[x][y][z];
	int ret=INF;
	if(!c_is_busy[x])ret=min(ret,f(x+1,y-1,0)+((z==0)?0:1));
	if(!j_is_busy[x])ret=min(ret,f(x+1,y,1)+((z==1)?0:1));
	return dp[x][y][z]=ret;
}
int main(){
	scanf("%d",&t);
	while(t--){
		scanf("%d %d",&ac,&aj);
		RESET(c_is_busy,0);
		RESET(j_is_busy,0);
		REP(i,ac){
			int x,y;
			scanf("%d %d",&x,&y);
			FOR(j,x,y-1)c_is_busy[j]=1;
		}
		REP(i,aj){
			int x,y;
			scanf("%d %d",&x,&y);
			FOR(j,x,y-1)j_is_busy[j]=1;
		}
		int an=INF;
		RESET(dp,-1);
		beginning=0;
		an=min(an,f(0,720,0));
		RESET(dp,-1);
		beginning=1;
		an=min(an,f(0,720,1));
		printf("Case #%d: %d\n",tc++,an);
	}
	return 0;
}