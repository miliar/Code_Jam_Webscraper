#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define fi first
#define se second
#define SZ(x) ((int)(x).size())
#define zero(x) (((x)>0?(x):-(x))<eps)
typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int>PII;
typedef pair<double,int>PDI;
const double eps=1e-8;
const double pi=acos(-1.0);
const int INF=0x3f3f3f3f;
const int mod=1e9+7;
LL powmod(LL a,LL b) {LL res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
int dp[1444][730][2],v[1444];
int main(){
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,cas=1,n,m,a,b;
    cin>>t;
    while(t--){
        cin>>n>>m;
        int sum0=0,sum1=0;
        memset(v,-1,sizeof v);
        memset(dp,INF,sizeof dp);
        for(int i=0;i<n;i++){
            cin>>a>>b;
            sum1+=b-a;
            for(int j=a+1;j<=b;j++) v[j]=1;
        }
        for(int i=0;i<m;i++){
            cin>>a>>b;
            sum0+=b-a;
            for(int j=a+1;j<=b;j++) v[j]=0;
        }
        dp[0][0][0]=0;
        for(int i=1;i<=1440;i++){
            for(int j=0;j<=min(i,720);j++){
                if(v[i]==0){
                    if(j){
                        dp[i][j][0]=min(dp[i][j][0],dp[i-1][j-1][0]);
                        dp[i][j][0]=min(dp[i][j][0],dp[i-1][j-1][1]+1);
                    }
                }
                else if(v[i]==1){
                    dp[i][j][1]=min(dp[i][j][1],dp[i-1][j][1]);
                    dp[i][j][1]=min(dp[i][j][1],dp[i-1][j][0]+1);
                }
                else {
                    if(j){
                        dp[i][j][0]=min(dp[i][j][0],dp[i-1][j-1][0]);
                        dp[i][j][0]=min(dp[i][j][0],dp[i-1][j-1][1]+1);
                    }
                    dp[i][j][1]=min(dp[i][j][1],dp[i-1][j][1]);
                    dp[i][j][1]=min(dp[i][j][1],dp[i-1][j][0]+1);
                }
            }
        }
        int ans=dp[1440][720][0];
        memset(dp,INF,sizeof dp);
        dp[0][0][1]=0;
        for(int i=1;i<=1440;i++){
            for(int j=0;j<=min(i,720);j++){
                if(v[i]==0){
                    if(j){
                        dp[i][j][0]=min(dp[i][j][0],dp[i-1][j-1][0]);
                        dp[i][j][0]=min(dp[i][j][0],dp[i-1][j-1][1]+1);
                    }
                }
                else if(v[i]==1){
                    dp[i][j][1]=min(dp[i][j][1],dp[i-1][j][1]);
                    dp[i][j][1]=min(dp[i][j][1],dp[i-1][j][0]+1);
                }
                else {
                    if(j){
                        dp[i][j][0]=min(dp[i][j][0],dp[i-1][j-1][0]);
                        dp[i][j][0]=min(dp[i][j][0],dp[i-1][j-1][1]+1);
                    }
                    dp[i][j][1]=min(dp[i][j][1],dp[i-1][j][1]);
                    dp[i][j][1]=min(dp[i][j][1],dp[i-1][j][0]+1);
                }
            }
        }
        printf("Case #%d: %d\n",cas++,min(ans,dp[1440][720][1]));
    }
    return 0;
}

