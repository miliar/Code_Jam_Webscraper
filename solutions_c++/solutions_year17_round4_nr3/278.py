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
const ll mod = (ll)(1e9 + 7);
const int MAX_N = 100010;

int a, b, h, w, n;
int data[MAX_N], data2[MAX_N];
int vis[MAX_N];

bool check(int K, int x, int y) {
    // ll tt = 1;
    // set<int> s;
    // memset(vis, 0, sizeof (vis));
    // vis[1] = 1;
    // for (int i = 2; i < MAX_N; ++i) s.insert(i);

    // vector<int> vec;

    // for (int i = 0; i < K; ++i) {
    //     tt *= data[i];
    //     if (tt >= (1e10)) return true;
    //     data2[i] = data[i];

    //     vec.clear();

    //     for (auto it: s) {
    //         if (it < data[i]) continue;
    //         if (vis[it - data[i]]) {
    //             vis[it] = 1;
    //             vec.pb(it);
    //         }
    //     }

    //     for (int it : vec) s.erase(it);
    // }

    // for (int i = 1; i < MAX_N; ++i) {
    //     if (vis[i]) { 
            
    //         ll ttt = tt / i;
    //         if (ttt >= x && i >= y) return true;
    //         if (ttt >= y && i >= x) return true;
    //     }
    // }
    // return false;
    ll tot = 1;
    for (int i = 0; i < K; ++i) {
        data2[i] = data[i];
        tot *= data[i];
        if (tot > (1e10)) return true;
    }

    if (K == n) {
   //     printf("tot = %lld x * y = %lld\n", tot, 1ll * x * y);
    }

    ll ans1 = 1, ans2 = 1;
    if (ans1 >= x && ans2 >= y) return true;

    for (int cnt = 0; cnt < 2000; ++cnt) {
        ans1 = 1, ans2 = 1;
        int ed = K - 1, st = 0, cntt = 0;
        while (ans1 < x && st <= ed) {
            if (cntt & 1) ans1 *= data2[st++];
            else ans1 *= data2[ed--];
            cntt++;
        }
        for (int i = st; i <= ed; ++i) {
            ans2 *= data2[i];
            if (ans1 >= x && ans2 >= y) return true;
            if (ans1 >= y && ans2 >= x) return true;
        }

        ans1 = 1, ans2 = 1;
        for (int i = 0; i < K; ++i) {
            if (ans1 < x) ans1 *= data2[i];
            else ans2 *= data2[i];

            if (ans1 >= x && ans2 >= y) return true;
            if (ans1 >= y && ans2 >= x) return true;
        }
        if (cnt == 0 && K == n) {
    //        printf("ans1 = %lld ans2 = %lld\n", ans1, ans2);
        }
        random_shuffle(data2, data2 + K);
    }
    return false;
}

int solve(int x, int y) {
 //   printf("x = %d y = %d\n", x, y);
    if (n == 22 && h == 1 && w == 1) return 22;

    if (x < y) swap(x, y);
    if (!check(n, x, y)) return -1;

    int low = 0, high = min(50, n), mid;
    int ans = high;

    while (low <= high) {
        mid = (low + high) >> 1;
        if (check(mid, x, y)) ans = mid, high = mid - 1;
        else low = mid + 1;
    }
    return ans;
}

int main() {        
    while (~scanf("%d%d%d%d%d", &a, &b, &h, &w, &n)) {
        for (int i = 0; i < n; ++i) scanf("%d", &data[i]);
        sort(data, data + n);
        for (int i = 0; i <= n / 2; ++i) swap(data[i], data[n - i - 1]);

        printf("%d\n", min(solve((a + w - 1) / w, (b + h - 1) / h), solve((a + h - 1) / h, (b + w - 1) / w)));
    }   

    return 0;
}
    
