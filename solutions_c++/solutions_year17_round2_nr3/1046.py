#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
#include<stdio.h>
#include<cmath>
#include<set>
#include<map>

using namespace std;

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T,k;
    string s;
    scanf("%d",&T);
    for(int t=1; t<=T; t++) {
        int q,n;
        int e[101],s[101],a[101][101];
        double dp[101][101];

        scanf("%d%d",&n,&q);
        for(int i=1; i<=n; i++)
            scanf("%d%d",&e[i],&s[i]);
        for(int i=1; i<=n; i++)
        for(int j=1; j<=n; j++) {
            scanf("%d",&a[i][j]);
        }
        cout<<"Case #"<<t<<": ";
        while(q--) {
            int st, fi;
            scanf("%d%d",&st,&fi);
            dp[2][1]=(double)a[1][2]/s[1];
            for(int i=3; i<=n; i++) {
                double dist=0;
                for(int j=i-1; j>=1; j--) {
                    dist+=a[j][j+1];
                    dp[i][j]=-1;
                    if(dist>e[j]) {
                        continue;
                    }
                    //printf("**  %d %d\n",i,j);
                    if(j==1) {
                        dp[i][j]=dist/(double)s[1];
                        continue;
                    }
                    for(int l=1; l<j; l++) {
                        if(dp[j][l] != -1) {
                            if(dp[i][j]==-1) dp[i][j]=dist/(double)s[j] + dp[j][l];
                            else
                            dp[i][j]=min(dp[i][j], dist/(double)s[j] + dp[j][l]);
                        }
                    }
                }
            }
            double ans=-1;
            for(int i=1; i<n; i++) {
                if(dp[n][i]==-1) continue;
                if(ans==-1) ans=dp[n][i];
                else ans=min(ans,dp[n][i]);
            }

            printf("%.6lf ",ans);
        }
        printf("\n");
    }
}
