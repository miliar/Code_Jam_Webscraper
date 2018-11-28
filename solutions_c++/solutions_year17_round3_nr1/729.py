#include <bits/stdc++.h>
#define va first
#define vb second
using namespace std;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
const double pi=acos(-1);
int N;
pii tam[1005];
double dp[1005][1005];

int main(){
    freopen("A-large.in","rt",stdin);
    freopen("A-large-output.out","wt",stdout);
    int T;
    scanf("%d",&T);
    for(int f=1;f<=T;f++){
        int K; cin>>N>>K;
        for(int i=0;i<N;i++) cin>>tam[i].va>>tam[i].vb;
        sort(tam,tam+N);
        for(int j=1;j<=K;j++){
            double M=0;
            for(int i=1;i<=N;i++){
                dp[j][i]=M+2.0*pi*tam[i-1].va*tam[i-1].vb;
                M=max(M,dp[j-1][i]);
            }
        }
        double ans=0;
        for(int i=1;i<=N;i++) ans=max(ans,dp[K][i]+pi*tam[i-1].va*tam[i-1].va);
        printf("Case #%d: %.9f\n",f,ans);
    }
}
