#include <cstdio>
#include <iostream>
using namespace std;

const int maxn = 105;

int xx;

struct H {
    double dist, speed;

    void scan() {
        cin>>xx;
        dist = (double)xx;
        cin>>xx;
        speed = (double)xx;
    }
};
H horses[maxn];

double mat[maxn][maxn];

double dp[maxn];

int main() {
    //freopen("in.txt", "r", stdin);
    freopen("C-small-attempt2.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int cases; cin>>cases;
    for(int caseno=1;caseno<=cases;caseno++) {
        int n, q, u, v;
        cin>>n>>q;
        for(int i=1;i<=n;i++) {
            horses[i].scan();
            dp[i] = 1e101;
        }
        for(int i=1;i<=n;i++) {
            for(int j=1;j<=n;j++) {
                cin>>mat[i][j];
            }
        }

        dp[1]=0.0;
        double d, s, t, c;
        for(int i=1;i<=n;i++) {
            c = dp[i];
            d = horses[i].dist;
            s = horses[i].speed;
            for(int j=i+1;j<=n;j++) {
                if(d-mat[j-1][j] > -1e-11) {
                    t = mat[j-1][j]/s;
                    c += t;
                    if(c<dp[j]) dp[j]=c;
                    d -= mat[j-1][j];
                }
                else break;
            }
        }

        printf("Case #%d:", caseno);
        while(q--) {
            cin>>u>>v;
            printf(" %.8lf\n", dp[n]);
        }
    }
    return 0;
}
