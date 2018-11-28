#include <bits/stdc++.h>
using namespace std;
long double ans[1100];
int N,K;
struct node{
int r,h;
node(){
r=h=0;
}
bool operator<(const node& t)const{
return r<t.r;
}
};
node aa[1100];
long long dp[1100][1100];
int main(){
//freopen("test","r",stdin);
int i,j,k,t,T,n,m;
scanf("%d",&T);
for(t=1;t<=T;t++){
scanf("%d%d",&N,&K);
for(i=1;i<=N;i++)
scanf("%d%d",&aa[i].r,&aa[i].h);
sort(aa+1,aa+N+1);
long long ans=-1,tmp;
memset(dp,0,sizeof(dp));
for(i=1;i<=N;i++){
for(j=1;j<=K;j++){
if(j>i)continue;
tmp=0;
for(k=0;k<=i-1;k++)
tmp=max(tmp,dp[k][j-1]+1ll*aa[i].r*aa[i].r-1ll*aa[k].r*aa[k].r+2ll*aa[i].h*aa[i].r);
for(int p=1;p<=i;p++)
tmp=max(tmp,dp[p][j]);
dp[i][j]=tmp;
}

}
/*for(i=1;i<=N;i++){
for(j=1;j<=N;j++)
printf("%lld ",dp[i][j]);
printf("\n");
}*/
printf("Case #%d: %lf\n",t,dp[N][K]*M_PI);
}
return 0;
}
