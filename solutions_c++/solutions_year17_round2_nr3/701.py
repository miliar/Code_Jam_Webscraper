#include <bits/stdc++.h>
using namespace std;
int Q,T,n,uk,vk;//,
const int maxn = 233;
double e[maxn],s[maxn],d[maxn][maxn];
double sum[maxn][maxn],dp[maxn][maxn];

int main(){
    cin>>T;
    freopen("c.txt","w",stdout);
    int _case = 0;
    while(T--){
        cin>>n>>Q;
        cout<<"Case #"<<++_case<<": ";
        for(int i=1;i<=n;i++)cin>>e[i]>>s[i];
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++)scanf("%d",&d[i][j]);//cin>>d[i][j];
        }
        while(Q--){
        cin>>uk>>vk;
        for(int i=1;i<=n;i++)for(int j=1;j<=n;j++)dp[i][j]=-1,sum[i][j]=-1;
        
        for(int i=n-1;i>=1;i--){
            if(e[i]>=(sum[n]-sum[i]))dp[i][n]=(sum[n]-sum[i])/s[i];
            for(int j=i+1;j<n;j++){
                if(e[i]>=(sum[j]-sum[i])){
                    double temp = (sum[j]-sum[i])/s[i]+dp[j][n];
                    //cout<<temp<<endl;
                    if(dp[i][n]!=-1) dp[i][n]=min(dp[i][n],temp);
                    else dp[i][n]=temp;
                }
            }
        }
        printf("%.9lf",dp[uk][vk]);}
    }
    return 0;
}
