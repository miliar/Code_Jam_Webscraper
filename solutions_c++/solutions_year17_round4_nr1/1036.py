#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/hash_policy.hpp>
#define f first
#define s second
//#pragma comment(linker,"/STACK:102400000,102400000")
using namespace std;
using namespace __gnu_pbds;
typedef pair<int,int> par;
typedef pair<int,par> pr;
int ar[10];
int dp[105][105][105];
int dp2[105][105];
int F(int a,int b,int c){
    if(!a&&!b&&!c)return 0;
    if(~dp[a][b][c])return dp[a][b][c];
    int ans=1;
    if(a)ans=max(ans,F(a-1,b,c));
    if(b)ans=max(ans,F(a,b-1,c));
    if(c)ans=max(ans,F(a,b,c-1));
    if(a&&c)ans=max(ans,F(a-1,b,c-1)+1);
    if(b>=2)ans=max(ans,F(a,b-2,c)+1);
    if(a>=2&&b)ans=max(ans,F(a-2,b-1,c)+1);
    if(c>=2&&b)ans=max(ans,F(a,b-1,c-2)+1);
    if(a>=4)ans=max(ans,F(a-4,b,c)+1);
    if(c>=4)ans=max(ans,F(a,b,c-4)+1);
    dp[a][b][c]=ans;
    return ans;
    }
int G(int a,int b){
    if(!a&&!b)return 0;
    if(~dp2[a][b])return dp2[a][b];
    int ans=1;
    if(a)ans=max(ans,G(a-1,b));
    if(b)ans=max(ans,G(a,b-1));
    if(a&&b)ans=max(ans,G(a-1,b-1)+1);
    if(a>=3)ans=max(ans,G(a-3,b)+1);
    if(b>=3)ans=max(ans,G(a,b-3)+1);
    dp2[a][b]=ans;
    return ans;
    }
int main(){
    int t,T=0;
    scanf("%d",&t);
    while(t--){T++;
        int n,p;
        scanf("%d%d",&n,&p);
        memset(ar,0,sizeof(ar));
        memset(dp,0,sizeof(dp));
        for(int i=0;i<n;i++){
            int x;
            scanf("%d",&x);
            ar[x%p]++;
            }
        int ans=0;
        ans+=ar[0];
        if(p==2){
            ans+=(ar[1]+1)/2;
            }
        else if(p==3){
            memset(dp2,-1,sizeof(dp2));
            int res=G(ar[1],ar[2]);
            int res2=0;
            int k=min(ar[1],ar[2]);
            res2+=k;
            ar[1]-=k;
            ar[2]-=k;
            res2+=ar[1]/3;
            ar[1]%=3;
            res2+=ar[2]/3;
            ar[2]%=3;
            res2+=(!!ar[1])+(!!ar[2]);
            if(res!=res2)puts("!!!!");
            ans+=res;
            }
        else if(p==4){
            memset(dp,-1,sizeof(dp));
            ans+=F(ar[1],ar[2],ar[3]);
            }
        printf("Case #%d: %d\n",T,ans);
        }
    return 0;
    }
