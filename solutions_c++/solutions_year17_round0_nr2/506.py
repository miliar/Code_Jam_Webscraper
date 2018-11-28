#include <bits/stdc++.h>
using namespace std;
#define PB push_back
#define ZERO (1e-10)
#define INF (1<<29)
#define CL(A,I) (memset(A,I,sizeof(A)))
#define DEB printf("DEB!\n");
#define D(X) cout<<"  "<<#X": "<<X<<endl;
#define EQ(A,B) (A+ZERO>B&&A-ZERO<B)
typedef long long ll;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
#define IN(n) int n;scanf("%d",&n);
#define FOR(i, m, n) for (int i(m); i < n; i++)
#define F(n) FOR(i,0,n)
#define FF(n) FOR(j,0,n)
#define FT(m, n) FOR(k, m, n)
#define aa first
#define bb second
void ga(int N,int *A){F(N)scanf("%d",A+i);}
char s[32],r[32];
bool dp[32][10][2];
ll N,X,L,I;
bool dfs(int u,int d,bool x){
    if(u==L)return 1;
    if(dp[u][d][x]++)return 0;
    if(!x){
        if(s[u]-48>=d&&dfs(u+1,s[u]-48,0))return r[u]=s[u],1;
        for(int i=s[u]-49;i>=d;--i)if(dfs(u+1,i,1))return r[u]=i+48,1;
    }else for(int i=9;i>=d;--i)if(dfs(u+1,i,1))return r[u]=i+48,1;
    return 0;
}
int main(void){
    IN(_)F(_){
        scanf("%lld",&N),sprintf(s,"%lld",N),L=strlen(s),CL(dp,0),CL(r,I=0);
        assert(dfs(0,0,0));
        while(r[I]==48)++I;
        printf("Case #%d: %s\n",i+1,r+I);
    }
    return 0;
}
