#include <bits/stdc++.h>

#define ff first
#define ss second
#define mp make_pair

using namespace std;

typedef long long ll;

const double PI = acos(-1);

pair<ll,ll> v[1005];
double dp[1005][1005];

double vol(int i, int j){
    return PI*((double)v[i].ff*v[i].ff - (double)v[j].ff*v[j].ff) + 2*PI*v[i].ff*v[i].ss;
}

int main(){
    int T;

    scanf("%d", &T);

    for(int t = 1; t <= T; t++){
        int n,k;

        scanf("%d%d", &n,&k);
        for(int i = 0; i < n; i++)
            scanf("%lld%lld", &v[i].ff, &v[i].ss);

        sort(v,v+n);
        memset(dp,0,sizeof dp);

        for(int i = 0; i < n; i++){
            dp[i][1] = (double)PI*v[i].ff*v[i].ff + 2*PI*v[i].ff*v[i].ss;

            for(int j = 0; j < i; j++){
                for(int m = 2; m <= k; m++){
                    dp[i][m] = max(dp[i][m], dp[j][m-1] + vol(i,j));
                }
            }
        }

        double ans = 0;
        for(int i = 0; i < n; i++)
            ans = max(ans, dp[i][k]);

        printf("Case #%d: %.15lf\n",t,ans);
    }
    
    return 0;
}