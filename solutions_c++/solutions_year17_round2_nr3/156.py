#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/hash_policy.hpp>
#define f first
#define s second
//#pragma comment(linker,"/STACK:102400000,102400000")
using namespace std;
using namespace __gnu_pbds;
typedef pair<long double,int> par;
long long int mp[105][105];
long double dp[105][105],one=1;
int e[105],s[105];
int main(){
    int t,T=0;
    scanf("%d",&t);
    while(t--){T++;
        int n,q;
        scanf("%d%d",&n,&q);
        for(int i=0;i<n;i++)
            scanf("%d%d",&e[i],&s[i]);
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++){
                scanf("%lld",&mp[i][j]);
                if(mp[i][j]==-1)mp[i][j]=0x3fffffffffffffffLL;
                }
        for(int k=0;k<n;k++)
            for(int i=0;i<n;i++)
                for(int j=0;j<n;j++)
                    mp[i][j]=min(mp[i][j],mp[i][k]+mp[k][j]);
        printf("Case #%d:",T);
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++){
                if(mp[i][j]>e[i])
                    dp[i][j]=INFINITY;
                else
                    dp[i][j]=one*mp[i][j]/s[i];
                }
        for(int k=0;k<n;k++)
            for(int i=0;i<n;i++)
                for(int j=0;j<n;j++)
                    dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j]);
        while(q--){
            int a,b;
            scanf("%d%d",&a,&b);a--;b--;
            printf(" %.15f",(double)dp[a][b]);
            }
        puts("");
        }
    return 0;
    }
