#include <bits/stdc++.h>
using namespace std;
template <class T> int size(const T &x) { return x.size(); }
#define rep(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)
#define iter(it,c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
const int INF = 2147483647;

int main() {
    int ts;
    cin >> ts;
    rep(t,0,ts) {
        int n, c, m;
        cin >> n >> c >> m;
        vi tneed(n), cnt(c);
        rep(i,0,m) {
            int a, b;
            cin >> a >> b;
            a--, b--;
            tneed[a]++;
            cnt[b]++;
        }
        int mx = 0;
        iter(it,cnt) mx = max(mx, *it);
        int lo = mx,
            hi = m,
            res = m+1,
            needed = 0;
        while (lo <= hi) {
            int mid = (lo+hi)/2;
            bool ok = true;
            vi have(n, mid),
               add(n, 0),
               need = tneed;

            int cur = 0;
            for (int i = n-1; i >= 0; i--) {
                int t = min(have[i], need[i]);
                have[i] -= t;
                need[i] -= t;

                t = min(have[i], add[i]);
                have[i] -= t;
                add[i] -= t;

                if (i == 0 && add[i] + need[i] > 0) {
                    ok = false;
                    break;
                }
                if (add[i] + need[i] > 0) {
                    cur += need[i];
                    add[i-1] += add[i] + need[i];
                }
            }
            if (ok) {
                hi = mid - 1;
                res = mid;
                needed = cur;
            } else {
                lo = mid + 1;
            }
        }
        cout << "Case #" << (t+1) << ": " << res << " " << needed << endl;
    }
    return 0;
}

