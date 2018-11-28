#include "bits/stdc++.h"
#define puba push_back
#define ff first
#define ss second
#define bend(_x) begin(_x), end(_x)
#define szof(_x) ((int) (_x).size())
#define cmpby(_x) [](const auto& a, const auto& b) {return (a _x) < (b _x);}
#define TASK_NAME ""

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
const int INF = 1e9 + 7;
const double PI = atan2(0, -1);
const int MAXN = 105;

bool check(int a, int q, int b) {
    return 9 * a * q <= b * 10 && b * 10 <= 11 * a * q;
}

map<int, int> have[MAXN];

int solve() {
    int n, p;
    scanf("%d%d", &n, &p);

    for (int i = 0; i < n; ++i) {
        have[i].clear();
    }

    vector<int> arr;
    for (int i = 0; i < n; ++i) {
        int num;
        scanf("%d", &num);
        arr.puba(num);
    }

    vector<tuple<int, int, int>> segs;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < p; ++j) {
            int num;
            scanf("%d", &num);
            ll l = 0, r = 1e6 + 5;
            while (r - l > 1) {
                ll mid = (l + r) / 2;
                if (9 * arr[i] * mid <= num * 10) {
                    l = mid;
                } else {
                    r = mid;
                }
            }

            int to = l;
            l = 0, r = 1e6 + 5;

            while (r - l > 1) {
                ll mid = (l + r) / 2;
                if (num * 10 <= 11 * arr[i] * mid) {
                    r = mid;
                } else {
                    l = mid;
                }
            }
            int from = r;

            if (from <= to) {
                segs.puba({from, 0, i});
                segs.puba({to, 1, i});
            }
        }
    }

    int ans = 0;

    sort(bend(segs));
    vector<int> cur(n);
    vector<int> skip(n);

    for (auto t : segs) {
        int ind = get<2>(t);
        if (get<1>(t) == 0) {
            cur[ind]++;
        } else {
            if (skip[ind]) {
                --skip[ind];
            } else {
                cur[ind]--;
            }
        }

        int num = INF;
        for (int i = 0; i < n; ++i) {
            num = min(num, cur[i]);
        }
        for (int i = 0; i < n; ++i) {
            cur[i] -= num;
            skip[i] += num;
        }
        ans += num;
    }

    cout << ans << "\n";
    
    return 0;
}

int main() {
    //freopen(TASK_NAME ".in", "r", stdin);
    //freopen(TASK_NAME ".out", "w", stdout);

    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }

    #ifdef LOCAL
        cerr << "time: " << clock() << endl;
    #endif
    return 0;
}