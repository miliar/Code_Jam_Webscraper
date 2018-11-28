#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int bit[100];
int dp[100][100];
bool vis[100][100];

ll dfs(int pos, int tail, bool limit){
    if (pos == -1) return 1;
    if (!limit && vis[pos][tail])
        return dp[pos][tail];
    int up = limit ? bit[pos] : 9;
    ll ret = 0;
    for (int i=tail; i<=up; i++){
        ret += dfs(pos-1, i, limit && i == up);
    }
    if (!limit){
        vis[pos][tail] = 1;
        dp[pos][tail] = ret;
    }
    return ret;
}
inline ll solve(ll x){
    bit[0] = x % 10;
    int len = 1;
    while (x /= 10){
        bit[len++] = x % 10;
    }
    return dfs(len-1, 0, 1);
}
int main(){
//    freopen("B-small-attempt0.in", "r", stdin);
//    freopen("B-small.out", "w", stdout);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    ll n;
    int test;
    scanf("%d", &test);
    for (int cas=1; cas<=test; cas++){
        scanf("%lld", &n);
        ll total = solve(n);
        ll L = 1, R = n;
        while (L <= R){
            ll mid = (L+R)>>1;
            ll tp = solve(mid);
            if (tp >= total)
                R = mid - 1;
            else
                L = mid + 1;
        }
        printf("Case #%d: %lld\n", cas, R+1);
    }
    return 0;
}
