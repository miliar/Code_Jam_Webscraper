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

map<vi,int> mem;
int dp(vi arr) {
    if (mem.find(arr) != mem.end())
        return mem[arr];
    int p = size(arr);
    int cnt = 0;
    iter(it,arr) cnt += *it;
    if (cnt == 0) return 0;
    int mn = cnt - 1;
    rep(x0,0,p+1) if (x0 == 0 || (0 < p && x0 <= arr[0]))
    rep(x1,0,p+1) if (x1 == 0 || (1 < p && x1 <= arr[1]))
    rep(x2,0,p+1) if (x2 == 0 || (2 < p && x2 <= arr[2]))
    rep(x3,0,p+1) if (x3 == 0 || (3 < p && x3 <= arr[3])) {
        if (x0 + x1 + x2 + x3 == 0) continue;
        if ((0 * x0 + 1 * x1 + 2 * x2 + 3 * x3) % p == 0) {
            vi nxt(arr);
            if (0 < p) nxt[0] -= x0;
            if (1 < p) nxt[1] -= x1;
            if (2 < p) nxt[2] -= x2;
            if (3 < p) nxt[3] -= x3;
            mn = min(mn, dp(nxt) + (x0 + x1 + x2 + x3 - 1));
        }
    }
    // iter(it,arr) {
    //     cout << *it << " ";
    // }
    // cout << ": " << mn << endl;
    return mem[arr] = mn;
}

int main() {
    int ts;
    cin >> ts;
    rep(t,0,ts) {
        int n, p;
        cin >> n >> p;
        vi arr(p);
        rep(i,0,n) {
            int x;
            cin >> x;
            arr[x % p]++;
        }
        cout << "Case #" << (t+1) << ": " << n - dp(arr) << endl;
    }
    return 0;
}

