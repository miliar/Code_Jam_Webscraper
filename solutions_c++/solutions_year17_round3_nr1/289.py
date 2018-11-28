#include <bits/stdc++.h>
using namespace std;
#define mp(X,Y) make_pair(X,Y)
#define F first
#define S second
typedef long long ll;
typedef pair<int,int> PII;
typedef pair<ll,ll> PLL;
int R[1010],h[1010];
PLL p[1010];
ll dp[1010];
int main(){
    ios::sync_with_stdio(0);
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int cas = 1;
    int t;
    long double pi = acos(-1.0);
    cin >> t;
    while(t--){
        cout << "Case #" << cas ++ << ": ";
        int n,k;
        cin >> n >>k;
        for(int i = 1 ; i<=n ; i++){
            cin >> p[i].first >> p[i].second;
        }
        sort(p + 1,p+n +1);
        dp[0] = 0;
        long long ans = 0;
        for(int i = 1 ; i <=n ; i ++){
            dp[i] = 0;
            for(int j = min(i,k);j > 0 ; j --){
                if(j == k){
                    ans = max(ans,dp[j-1]+2 * p[i].first * p[i].second + p[i].first * p[i].first);
                }
                dp[j] = max(dp[j],dp[j-1] + 2 * p[i].first * p[i].second);
            }
        }
        cout << fixed <<setprecision(10) << ans * pi  <<endl;



    }
    return 0;
}
