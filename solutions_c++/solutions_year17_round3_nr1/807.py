#include <bits/stdc++.h>
#include <ext/numeric>
#include <ext/rope>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/hash_policy.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/priority_queue.hpp>
using namespace __gnu_cxx;
using namespace __gnu_pbds;
template<typename T>
using pbq = priority_queue<T>;
using namespace std;
using LL = int64_t;
using LD = long double;
const int INF = 0x3f3f3f3f;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    fstream cin("A-large.in");
    fstream cout("out.txt");
    const LD PI = acos(-1);
    struct node {
        LD val;
        int num;
    };
    int t;
    cin >> t;
    int T = t;
    while (t--) {
        cout << "Case #" << T - t << ": ";
        int n, k;
        cin >> n >> k;
        vector<node> r(n), h(n);
        for (int i = 0; i < n; i++) {
            r[i].num = h[i].num = i;
            cin >> r[i].val >> h[i].val;
            h[i].val = 2 * PI * r[i].val * h[i].val;
            r[i].val = PI * r[i].val * r[i].val;
        }
        sort(r.begin(), r.end(), [](node& a, node& b) {return a.val > b.val;});
        sort(h.begin(), h.end(), [](node& a, node& b) {return a.val > b.val;});
        vector<int> us(n);
        LD ans = 0;
        for (int i = 0; i < n; i++) {
            LD sum = r[i].val;
            us[r[i].num] = 1;
            int s = k - 1;
            for (int j = 0; j < n; j++) {
                if (s && us[h[j].num] == 0 || h[j].num == r[i].num) {
                    sum += h[j].val;
                    if (h[j].num != r[i].num) s--;
                } 
            }
            if (!s) ans = max(ans, sum);
            else break;
        }
        cout << fixed << setprecision(9) << ans << endl;
    }
}
