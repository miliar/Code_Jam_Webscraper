#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <deque>
#include <map>
#include <set>
#include <vector>
typedef long long ll;
using namespace std;
ll dp[55][55];
int num[55];
ll dfs(int cnt, int st, int pre, int f) {
    if(cnt < 1) {
        return pre == 1;
    }
    if(!f && pre && dp[cnt][st] != -1) return dp[cnt][st];
    ll sum = 0;
    int end = f? num[cnt] : 9;
    for(int i = st; i <= end; ++i) {
        sum += dfs(cnt-1, i, pre ||i != 0, f && i == end);
    }
    if(!f && pre) dp[cnt][st] = sum;
    return sum;
}
ll solve(ll x) {

    int cnt = 0;
    while(x) {
        num[++cnt] = x%10;
        x /= 10;
    }
    return dfs(cnt, 0, 0, 1);
}
int main(){
    memset(dp, -1, sizeof(dp));
    int T, ca = 1;
    scanf("%d", &T);
    while(T--) {
        ll n;
        scanf("%lld", &n);
        ll tmp = solve(n);
        ll l = 1, r = n, ans = -1;
        while(l <= r) {
            ll mid = (l+r) >> 1;
            if(solve(mid) >= tmp) {
                r = mid-1;
                ans = mid;
            }
            else l = mid+1;
        }
        printf("Case #%d: %lld\n", ca++, ans);
    }
}
