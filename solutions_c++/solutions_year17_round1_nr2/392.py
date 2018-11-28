#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
#include <vector>
#define ll long long
#define maxn 200010
using namespace std;
struct edge{
    int to,next;
}e[maxn<<1];
int box[maxn],cnt,in[maxn];
void init(){
    memset(box,-1,sizeof(box));
    cnt=0;
}
void add(int from,int to){
    e[cnt].to=to;
    e[cnt].next=box[from];
    box[from]=cnt++;
}
int dp[maxn][3];
void dfs(int now,int fa){
    int ma1=-3000000,ma2=-3000000;
    for(int t=box[now];t+1;t=e[t].next){
        int v=e[t].to;
        if(v!=fa){
            dfs(v,now);
            int tmp=max(dp[v][0],max(dp[v][1],dp[v][2]));
            int tp2=max(dp[v][1],dp[v][0]);
            dp[now][0]+=tmp;
            dp[now][1]+=tmp;
            dp[now][2]+=tmp;
            if(tp2-tmp>ma1){
                ma2=ma1;
                ma1=tp2-tmp;
            }
            else if(tp2-tmp>ma2){
                ma2=tp2-tmp;
            }
        }
    }
    dp[now][1]+=ma1+1;
    dp[now][2]+=2+ma1+ma2;
}
int main()
{
    freopen("dd.txt","r",stdin);
    ll n,x,y;
    cin>>n>>x>>y;
    init();
    for(int i=1;i<n;i++){
        int u,v;
        scanf("%d%d",&u,&v);
        add(u,v);
        add(v,u);
        in[u]++;
        in[v]++;
    }
    if(x>=y){
        bool flag=false;
        for(int i=1;i<=n;i++){
            if(in[i]==n-1)
                flag=true;
        }
        if(flag)
            cout<<(n-2)*y+x;
        else
            cout<<(n-1)*y;
    }
    else{
        dfs(1,0);
        /*for(int i=1;i<=n;i++){
            printf("%d dp0=%d dp1=%d dp2=%d\n",i,dp[i][0],dp[i][1],dp[i][2]);
        }*/
        int num=max(dp[1][0],max(dp[1][1],dp[1][2]));
        cout<<x*num+(n-1-num)*y<<endl;
    }
    return 0;
}
