#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
#define ll long long
using namespace std;
const int N=20;
char str[N];

long long n;
int dig[N],len;
void getdig(long long x)
{
    len=0;
    while(x)
    {
        dig[++len]=x%10;
        x/=10;
    }
}

ll ans;
ll dp[N][10][2][2];
void dfs(int pos,int pre,int status,int has,int up,ll num)
{
    if(status==0){
        dp[pos][pre][has][up]=0;
        return ;
    }
    if(pos<=0){
        if(status&&ans==0){
            ans = num;
        }
        return ;
    }
    if(!up&&dp[pos][pre][has][up]==0) {
        return ;
    }
    int ed = up?dig[pos]:9;
    ll ans=0;
    for(int i=ed;i>=0;i--){
      //  ans=dfs(pos-1,i,status&&(pre==-1||i>=pre),up&&(i==ed),num*10+i);
        if(has){
            dfs(pos-1,i,status,has&&i==0,up&&i==ed,num*10+i);
        }else{
            dfs(pos-1,i,status&&i>=pre,has&&i==0,up&&i==ed,num*10ll+i);
        }

    }
    return ;
}

int main()
{
     freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);


    for(int ca=1;ca<=T;ca++)
    {
        ll n;
        cin>>n;
        memset(dp,-1,sizeof(dp));ans=0;
        getdig(n);
      //  for(int i=len;i>=1;i--){ printf("%d ",dig[i]);}puts("");
        dfs(len,0,1,1,1,0);
        printf("Case #%d: %lld\n",ca,ans);
    }
    return 0;
}
