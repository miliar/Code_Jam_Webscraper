#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const double inf=1e15;
const int INF =1e9+10;
int n,q;
int e[109],s[109];
int d[109][109];
int dp[109];
double t[109][109];
bool vi[109];
priority_queue<P,vector<P>,greater<P> > pr;
void dfs(int x){
    for(int i=0;i<n;++i)vi[i]=0,dp[i]=INF;
    dp[x]=0;
    while(!pr.empty())pr.pop();
    pr.push(P(0,x));
    while(!pr.empty()){
        int u=pr.top().second;
        pr.pop();
        if(vi[u])continue;
        vi[u]=1;
        int &no=dp[u];
        for(int i=0;i<n;++i){
            if(d[u][i]!=-1&&no+d[u][i]<=e[x]&&dp[i]>no+d[u][i]){
                dp[i]=no+d[u][i];
                pr.push(P(dp[i],i));
            }
        }
    }
    for(int i=0;i<n;++i){
        t[x][i]=inf;
        if(dp[i]!=INF)t[x][i]=(double)dp[i]/s[x];
    }
}
int main(){
    freopen("C-small-attempt0.in","r",stdin);
//    freopen("C-large.in","r",stdin);
    freopen("C.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;++ca){
        scanf("%d%d",&n,&q);
        for(int i=0;i<n;++i)scanf("%d%d",&e[i],&s[i]);
        for(int i=0;i<n;++i){
            for(int j=0;j<n;++j)scanf("%d",&d[i][j]);
        }
        for(int i=0;i<n;++i)dfs(i);
        for(int i=0;i<n;++i){
            for(int j=0;j<n;++j)
                for(int k=0;k<n;++k)
                if(t[j][k]>t[j][i]+t[i][k])t[j][k]=t[j][i]+t[i][k];
        }
        printf("Case #%d: ",ca);
        for(int i=0;i<q;++i){
            int q,w;
            scanf("%d%d",&q,&w);
            printf("%.9f%c",t[q-1][w-1]," \n"[i==q-1]);
        }
    }
    return 0;
}
