#include<bits/stdc++.h>
#include <math.h>
using namespace std;
#define pb push_back
#define ll long long
#define pii pair<int,int>
#define vi vector<int>
#define vb vector<bool>
#define vii vector<pii>
#define pllll pair<ll,ll>
#define vll vector<ll>
#define vllll vector<pllll>
void solve(){
    int n,k;
    scanf("%d %d",&n,&k);
    vector<double> v(n);
    double u;
    scanf("%lf",&u);
    for(int i=0;i<n;i++){
        scanf("%lf",&v[i]);
    }
    sort(v.begin(),v.end(),greater<double>());
    double sumk=u;
    for(int i=0;i<k;i++){
        sumk+=v[i];
    }
    for(int i=0;i<k;i++){
        double vv=sumk/(k-i);
        if(vv>=v[i]){
            for(;i<k;i++){
                v[i]=vv;
            }
            break;
        }
        sumk-=v[i];
    }
    double dp[n+1][k];
    for(int i=0;i<k;i++)dp[0][i]=0;
    dp[0][0]=1;
    for(int i=1;i<=n;i++){
        for(int j=0;j<k;j++){
            if(j>i)dp[i][j]=0;
            else if(j==0){
                dp[i][j]=dp[i-1][j]*(1-v[i-1]);
            }
            else{
                dp[i][j]=(v[i-1])*dp[i-1][j-1]+(1-v[i-1])*dp[i-1][j];
            }
        }
    }
    double ans=1;
    for(int i=0;i<k;i++)ans-=dp[n][i];
    printf("%lf\n",ans);
}
int main(){
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        printf("Case #%d: ",i);
        solve();
    }
}
