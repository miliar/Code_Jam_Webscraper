#include<bits/stdc++.h>

using namespace std;

double dp[105];

long long a[105],b[105];

long long d[105][105];

int main(){

    freopen("gcj_in.txt","r",stdin);
    freopen("gcj_out.txt","w",stdout);

    int t;
    cin >> t;
    for(int it=1;it<=t;it++) {

        long long n,i,q,x=0,j,y=0;
        cin >> n >> q;
        for(i=1;i<=n;i++) {
            cin >> a[i] >> b[i];
        }
        for(i=1;i<=n;i++) {
            for(j=1;j<=n;j++) {
                cin >> d[i][j];
            }
        }
        while(q--) {
            cin >> x >> y;
            dp[1] = 0;
            for(i=2;i<=n;i++) {
                dp[i] = (double) 1e12;
            }
          //  printf("%0.8f\n",dp[n]);
            for(i=2;i<=n;i++) {
                x = 0;
                for(j=i-1;j>=1;j--) {
                    x = x + d[j][j + 1];
                    if(x <= a[j]) {
                        dp[i] = min(dp[i],dp[j] + ((double) x / (double) b[j]));
                    }
                }
            }
            cout << "Case #" << it << ": ";
            printf("%0.8f\n",dp[n]);
        }
    }
    return 0;


}
