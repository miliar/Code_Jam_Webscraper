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
#define F first
#define S second
const int INF=1e9;
const int MOD=1e9+7;
int t,tc=1,n,p,g[100],dp[101][101][101][4];
int f(int x,int y,int z,int leftover){
    if(x+y+z==0)return 0;
    if(dp[x][y][z][leftover]!=-1)return dp[x][y][z][leftover];
    int ret=0;
    if(x>0)ret=max(ret,f(x-1,y,z,(p-((1+(p-leftover)%p)%p))%p)+((leftover==0)?1:0));
    if(y>0)ret=max(ret,f(x,y-1,z,(p-((2+(p-leftover)%p)%p))%p)+((leftover==0)?1:0));
    if(z>0)ret=max(ret,f(x,y,z-1,(z-((3+(p-leftover)%p)%p))%p)+((leftover==0)?1:0));
    return dp[x][y][z][leftover]=ret;
}
int main(){
    freopen("a_small.in","r",stdin);
    freopen("a_small.out","w",stdout);
    scanf("%d",&t);
    while(t--){
        scanf("%d %d",&n,&p);
        REP(i,n)scanf("%d",&g[i]);
        int cnt[4]={0};
        REP(i,n)cnt[g[i]%p]++;
        RESET(dp,-1);
        int an=f(cnt[1],cnt[2],cnt[3],0);
        printf("Case #%d: %d\n",tc++,an+cnt[0]);
    }
    return 0;
}
