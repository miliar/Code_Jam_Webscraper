#include <bits/stdc++.h>
#define IOS ios_base::sync_with_stdio(0); cin.tie(0);
using namespace std;
typedef long long ll;
#define mp make_pair
#define fi first
#define se second
#define pb push_back

const double pi = acos(-1.0);
const int inf = 0x3f3f3f3f;
const ll INF = 0x3f3f3f3f3f3f3f3fll;
const int MAX_N = 10010;

int T, cases = 0;
ll n, K;
bool have;

ll calc(ll now, ll k) {
    if (now > 0 && (now - 1) / 2 >= k) {
        if (now == k * 2 + 2) have = true;
        return calc((now - 1) / 2, k) + calc(now / 2, k) + 1;
    } else {
        return 0;
    }
}

int main() {    
    freopen("3.in", "r", stdin);
    freopen("3.out", "w", stdout);

    scanf("%d", &T);
    while (T--) {
        scanf("%lld%lld", &n, &K);
        
        if ((K - 1) * 2 >= n) {
            printf("Case #%d: 0 0\n", ++cases);
            continue;
        }

        ll low = 0, high = n, mid, ans = 0;
        bool finalHave = false;
        while (low <= high) {
            mid = (low + high) >> 1;
            have = false;
            ll num = calc(n, mid);
            if (num >= K) {
           //     printf("mid = %lld num = %d\n", mid, num);
                ans = mid, low = mid + 1;
                finalHave = false;
                if (num > K || have) finalHave = true;
            } else high = mid - 1;
        }

        ll Max = ans;
        if (finalHave) Max++;

        printf("Case #%d: %lld %lld\n", ++cases, Max, ans);
    }
    return 0;
}
    
