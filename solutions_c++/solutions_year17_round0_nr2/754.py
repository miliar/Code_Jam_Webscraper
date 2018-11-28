#include <bits/stdc++.h>
using namespace std;

#define REPU(i, a, b) for (int i = (a); i < (b); ++i)
#define REPD(i, a, b) for (int i = (a); i > (b); --i)
#define FOREACH(it, a) for (auto it = a.begin(); it != a.end(); ++it)
#define MEM(a, x) memset(a, x, sizeof(a))
#define ALL(a) a.begin(), a.end()
#define UNIQUE(a) a.erase(unique(ALL(a)), a.end())

typedef long long ll;
const int MOD = 1000000007;

template<class T, class U> inline T tmin(T a, U b) { return (a < b) ? a : b; }
template<class T, class U> inline T tmax(T a, U b) { return (a > b) ? a : b; }
template<class T, class U> inline void amax(T &a, U b) { if (b > a) a = b; }
template<class T, class U> inline void amin(T &a, U b) { if (b < a) a = b; }
template<class T> inline T tabs(T a) { return (a > 0) ? a : -a; }
template<class T> T gcd(T a, T b) { while (b != 0) { T c = a; a = b; b = c % b; } return a; }

ll dp[20][10], sum[20];
int digits[30];

ll count(ll n) {
    if (n == 0) return 1;
    int idx = 0;
    while (n > 0) {
        digits[idx++] = n % 10;
        n /= 10;
    }
    reverse(digits, digits + idx);
    ll ans = sum[idx - 1];
    REPU(i, 0, idx) {
        int pre = i == 0 ? 0 : digits[i - 1];
        if (digits[i] < pre) break;
        REPU(j, pre, digits[i]) {
            ans += dp[idx - i][j];
        }
        if (i == idx - 1) ans++;
    }
    return ans;
}

int main(int argc, char *argv[]) {
	ios_base::sync_with_stdio(false);

    MEM(dp, 0);
    REPU(d, 0, 10) dp[1][d] = 1;
    REPU(l, 2, 20) REPU(d, 1, 10) {
        dp[l][d] = 0;
        REPU(i, d, 10) dp[l][d] += dp[l - 1][i];
    }
    sum[1] = 10;
    REPU(i, 2, 20) {
        sum[i] = sum[i - 1];
        REPU(j, 1, 10) sum[i] += dp[i][j];
    }
    
    int ntest; cin >> ntest;
    REPU(it, 1, ntest + 1) {
        ll n; cin >> n;
        ll tot = count(n);
        ll lb = 1, rb = n + 1;
        while (rb - lb > 1) {
            ll mb = (lb + rb) >> 1;
            if (tot > count(mb - 1)) lb = mb;
            else rb = mb;
        }
        printf("Case #%d: %lld\n", it, lb);
    }
	
	return 0;
}
