#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
#define LL long long

int n,q;
LL e[105],s[105];
LL dp[105][105];
double ans[105][105];

int main() {
    int tc;
    scanf("%d",&tc);
    for (int t=1; t<=tc; t++) {
        scanf("%d%d",&n,&q);
        for (int i=0; i<n; i++)
            scanf("%lld%lld",&e[i],&s[i]);
        for (int i=0; i<n; i++)
            for (int j=0; j<n; j++) {
                scanf("%lld",&dp[i][j]);
                ans[i][j] = 1e15;
            }
        for (int i=0; i<n; i++)
            for (int j=0; j<n; j++)
                for (int k=0; k<n; k++) {
                    if (dp[i][k] != -1 && dp[k][j] != -1 && ((dp[i][j] == -1) || (dp[i][k]+dp[k][j] < dp[i][j]))) {
                        dp[i][j] = dp[i][k] + dp[k][j];
                    }
                }
        /*
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++)
                printf("%lld ",dp[i][j]);
            printf("\n");
        }
        */
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++)
                if (dp[i][j] != -1 && dp[i][j] <= e[i])
                    ans[i][j] = dp[i][j] * 1.0 / s[i];
            ans[i][i] = 0;
        }
        /*
        printf("\n");
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++)
                printf("%.2f ",ans[i][j]);
            printf("\n");
        }
        printf("\n");
        */
        int rep = n;
        while (rep--) {
            for (int i=0; i<n; i++)
                for (int j=0; j<n; j++)
                    for (int k=0; k<n; k++) {
                        if (ans[i][k]+ans[k][j] < ans[i][j]) {
                            ans[i][j] = ans[i][k] + ans[k][j];
                        }
                    }
        }
        /*
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++)
                printf("%.2f ",ans[i][j]);
            printf("\n");
        }
        */

        printf("Case #%d:",t);
        for (int i=0; i<q; i++) {
            int u,v;
            scanf("%d%d",&u,&v);
            printf(" %.9f",ans[u-1][v-1]);
        }
        printf("\n");

    }
	return 0;
}
