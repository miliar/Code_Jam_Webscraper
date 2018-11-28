#include<bits/stdc++.h>
#define M_PI 3.14159265358979323846
using namespace std;
typedef long long ll;
struct P{
    int r,h;
};
bool cmp(P p1,P p2){
    if(p1.r==p2.r){
        return (p1.h>p2.h);
    }
    return (p1.r>p2.r);
}
ll y(int r,int h){
    return (2LL*((ll)r)*((ll)h));
}
ll z(int r,int h){
    return (((ll)r*(ll)r)+y(r,h));
}
int main(){
    int t,x,k,i,n,j;
    cin>>t;
    for(x=1;x<=t;x++){
        cin>>n>>k;
        P p[n];
        for(i=0;i<n;i++){
            cin>>p[i].r>>p[i].h;
        }
        cout<<"Case #"<<x<<": ";
        sort(p,p+n,cmp);
        ll dp[n][k+1];
        for(i=0;i<n;i++){
            for(j=0;j<=k;j++){
                dp[i][j]=0;
            }
        }
        dp[0][1]=z(p[0].r,p[0].h);
        for(i=1;i<n;i++){
            dp[i][1]=max(dp[i-1][1],z(p[i].r,p[i].h));
            for(j=2;j<=k&&j<=(i+1);j++){
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+y(p[i].r,p[i].h));
            }
        }
        long double ans=dp[n-1][k],y=M_PI;
        printf("%.9Lf\n",ans*y);
    }
    return 0;
}
