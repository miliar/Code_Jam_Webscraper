#include <bits/stdc++.h>
using namespace std;
int n,p,ans;
int num[4];
int dp4[109][109][109][4];
int dp3[109][109][3];
int dfs3(int a,int b,int c){
    if(a==0&&b==0)return 0;
    if(dp3[a][b][c]!=-1)return dp3[a][b][c];
    int ans=0;
    if(a)ans=max(ans,(c==0)+dfs3(a-1,b,(c+1)%3));
    if(b)ans=max(ans,(c==0)+dfs3(a,b-1,(c+2)%3));
    return dp3[a][b][c]=ans;
}
int dfs4(int a,int b,int c,int d){
    if(a==0&&b==0&&c==0)return 0;
    if(dp4[a][b][c][d]!=-1)return dp4[a][b][c][d];
    int ans=0;
    if(a)ans=max(ans,(d==0)+dfs4(a-1,b,c,(d+1)%4));
    if(b)ans=max(ans,(d==0)+dfs4(a,b-1,c,(d+2)%4));
    if(c)ans=max(ans,(d==0)+dfs4(a,b,c-1,(d+3)%4));
    return dp4[a][b][c][d]=ans;
}
int main(){
//    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    memset(dp4,-1,sizeof dp4);
    memset(dp3,-1,sizeof dp3);
    for(int ca=1;ca<=T;++ca){
        scanf("%d%d",&n,&p);
        memset(num,0,sizeof num);
        for(int i=0;i<n;++i){
            int g;
            scanf("%d",&g);
            ++num[g%p];
        }
        ans=num[0];
        printf("Case #%d: ",ca);
        if(p==2){
            ans+=(num[1]+1)/2;
        }
        else if(p==3){
            ans+=dfs3(num[1],num[2],0);
        }
        else if(p==4){
            ans+=dfs4(num[1],num[2],num[3],0);
        }
        printf("%d\n",ans);
    }
    return 0;
}
