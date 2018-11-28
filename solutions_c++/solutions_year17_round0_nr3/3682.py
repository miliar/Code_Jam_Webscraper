#include <bits/stdc++.h>

using namespace std;

using ll = long long;

#define clr(a) (a.clear())
#define sz(x) (int)x.size()
#define mem(a,b) memset(a, b, sizeof(a))
#define Unique(store) store.resize(unique(store.begin(),store.end())-store.begin())
#define pb push_back
#define FAST ios_base::sync_with_stdio(0);cin.tie(0);

#define X first
#define Y second

using pii = pair <int, int>;
using pll = pair <ll, ll>;

const ll inf = 1;
const ll mod = 1E9;


#define SZ 100010

struct data {
    int a, b, range;
    data () {}
    data (int x, int y) {
        a = x, b = y;
        range = b - a - 1;
    }
    bool operator < (const data& p) const {
        if (range == p.range)
            return a > p.a;
        return range < p.range;
    }
};


int main() {
//#if defined JESI
//        freopen("C-small-2-attempt0.in", "r", stdin);
//        freopen("3.txt", "w", stdout);
//#endif

    ios::sync_with_stdio(false);

    int t;
    cin >> t;

    for (int cs = 0; cs < t; cs++) {
        int n, k;
        cin >> n >> k;

        priority_queue <data> pq;
        pq.push(data(0, n + 1));

        int mx, mn;

        for (int i = 1; i <= k; i++) {
            data x = pq.top(); pq.pop();
            int mid = x.a + (x.range / 2) + (x.range % 2);

            pq.push(data(x.a, mid));
            pq.push(data(mid, x.b));

            if (i == k) {
                mx = max(mid - x.a - 1, x.b - mid - 1);
                mn = min(mid - x.a - 1, x.b - mid - 1);
            }
        }

        cout << "Case #" << cs + 1 << ": " << mx << " " << mn << endl;
    }

    return 0;
}




