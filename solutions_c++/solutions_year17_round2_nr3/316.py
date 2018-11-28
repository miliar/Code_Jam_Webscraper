#include<bits/stdc++.h>
using namespace std;
#define x first
#define y second
typedef long long int LL;
LL ma[105][105];
double dp[105][105];
int main(){
    int t, C=0;
    scanf("%d",&t);
    while(t--){
        int n,q;
        scanf("%d%d",&n,&q);
        vector<pair<LL, double>> arr;
        for(int i=0;i<n;i++){
            LL e;
            double s;
            scanf("%lld%lf",&e,&s);
            arr.push_back({e,s});
        }
        for(int i=0;i<n;i++)
        for(int j=0;j<n;j++){
            scanf("%lld",&ma[i][j]);
            dp[i][j]=-1;
        }
        for(int i=0;i<n;i++) ma[i][i]=0,dp[i][i]=0;
        for(int k=0;k<n;k++){
            for(int i=0;i<n;i++){
                for(int j=0;j<n;j++){
                    if(ma[i][k]==-1 || ma[k][j]==-1) continue;
                    if(ma[i][j]==-1 || ma[i][k]+ma[k][j]<ma[i][j]){
                        ma[i][j]=ma[i][k]+ma[k][j];
                    }
                }
            }
        }
        for(int i=0;i<n;i++)
        for(int j=0;j<n;j++){
            if(ma[i][j]==-1 || ma[i][j]>arr[i].x) continue;
            dp[i][j] = ma[i][j] / arr[i].y;
        }
        /*for(int i=0;i<n;i++){
            for(int j=0;j<n;j++)
                printf("%f ",dp[i][j]);
            puts("");
        }*/
        for(int k=0;k<n;k++){
            for(int i=0;i<n;i++){
                for(int j=0;j<n;j++){
                    if(dp[i][k]==-1 || dp[k][j]==-1) continue;
                    if(dp[i][j]==-1 || dp[i][k]+dp[k][j]<dp[i][j]){
                        dp[i][j]=dp[i][k]+dp[k][j];
                    }
                }
            }
        }
        /*for(int i=0;i<n;i++){
            for(int j=0;j<n;j++)
                printf("%f ",dp[i][j]);
            puts("");
        }*/
        vector<double> ans;
        while(q--){
            int a,b;
            scanf("%d%d",&a,&b);
            a--,b--;
            ans.push_back(dp[a][b]);
        }
        printf("Case #%d:",++C);
        for(int i=0;i<ans.size();i++) printf(" %f",ans[i]);
        puts("");
    }
}
