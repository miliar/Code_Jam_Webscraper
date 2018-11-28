#include <bits/stdc++.h>
using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define fore(i, b, e) for (int i = (int)(b); i <= (int)(e); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define pb push_back
#define fi first
#define se second
#define all(x) (x).begin(), (x).end()
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long i64;
typedef unsigned long long u64;
typedef long double ld;
typedef long long ll;

const int maxn = 1050;

int n, m, c;
int cnt[maxn];
int sum[maxn];

int can(int sz) {
    if (sz < *max_element(sum, sum+c)) {
        return -1;
    }
    int over = 0;
    int slots = 0;
    forn(i, n) {
        int cur = cnt[i];
        if (cur >= sz) {
            cur -= sz;
            if (cur > slots) {
                return -1;
            }
            over += cur;
            slots -= cur;
        } else {
            slots += sz - cur;
        }
    }
    return over;
}

void solve(int tn) {
    cin >> n >> c >> m;
    memset(cnt, 0, sizeof cnt);
    memset(sum, 0, sizeof sum);
    forn(i, m) {
        int p, b;
        cin >> p >> b;
        ++sum[b-1];
        ++cnt[p-1];
    }
    int l = 0, r = m;
    assert(can(r) > -1);
    assert(can(l) == -1);
    while (l+1 < r) {
        int m = (l+r)/2;
        if (can(m) != -1) {
            r = m;
        } else {
            l = m;
        }
    }

    int res = can(r);
    cout << "Case #" << tn << ": " << r << " " << res << endl;
}

int main() {
#ifdef LOCAL
//     freopen("b.in", "r", stdin);
#endif

    int t;
    cin >> t;
    forn(i, t) {
        solve(i+1);
    }


#ifdef LOCAL
    cerr << "Time elapsed: " << clock() / 1000 << " ms" << endl;
#endif
    return 0;
}
