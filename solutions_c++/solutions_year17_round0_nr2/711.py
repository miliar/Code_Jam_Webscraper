#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
#define first fi
#define second se
#define sz(x) (int)x.size()
const int inf = 0x3f3f3f3f;
const int mod = 1e9+7;
const int N = 25;

int T;
ll n;
int bit[N], bn;

bool judge(ll x) {
    bn = 0;
    if (!x) bit[bn++] = 0;
    while (x) {
        bit[bn++] = x % 10;
        x /= 10;
    }
    for (int i = 0; i < bn - 1; i++)
        if (bit[i] < bit[i + 1]) return false;
    return true;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int cas = 0;
    scanf("%d", &T);
    while (T--) {
        scanf("%lld", &n);
        ll s = 1, ans = 0;
        if (judge(n)) ans = n;
        for (int i = 0; i < 19; i++) {
            if (s > n) break;
            if (judge(n / s * s - 1))
                ans = max(n / s * s - 1, ans);
            s *= 10;
        }
        printf("Case #%d: %lld\n", ++cas, ans);
    }
    return 0;
}
