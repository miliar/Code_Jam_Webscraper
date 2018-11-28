#include <set>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 1010;
const int P = 2000010;

int T, n, p, r[N], a[N][N];
bool on[55][55], us[55][55];
set < pair <int, int> > ss[N];
vector < pair < int, pair <int, int> > > ev[P];

bool f9(long long m, long long x, int id) {
    long long v = m * r[id];
    return x * 10 >= v * 9;
}

bool f11(long long m, long long x, int id) {
    long long v = m * r[id];
    return x * 10 <= v * 11;
}

int main() {

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        scanf("%d %d", &n, &p);
        for (int i = 0; i < n; i++) {
            scanf("%d", &r[i]);
        }
        memset(on, false, sizeof on);
        memset(us, false, sizeof us);
        for (int i = 0; i < n; i++) {
            ss[i].clear();
        }
        for (int i = 0; i < P; i++) {
            ev[i].clear();
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                scanf("%d", &a[i][j]);
                int lo = 1;
                int hi = 2000000;
                while (lo <= hi) {
                    long long m = (lo + hi) / 2;
                    if (f9(m, a[i][j], i)) {
                        lo = m + 1;
                    } else {
                        hi = m - 1;
                    }
                }
                int p9 = hi;
                lo = 1;
                hi = p9;
                while (lo <= hi) {
                    long long m = (lo + hi) / 2;
                    if (f11(m, a[i][j], i)) {
                        hi = m - 1;
                    } else {
                        lo = m + 1;
                    }
                }
                int p11 = lo;
                if (p11 <= p9) {
                    ev[p11].push_back({p9, {i, j}});
                    ev[p9 + 1].push_back({-1, {i, j}});
                }
            }
        }
        int ans = 0;
        for (int i = 1; i < P; i++) {
            for (int j = 0; j < ev[i].size(); j++) {
                if (ev[i][j].first != -1 && !us[ev[i][j].second.first][ev[i][j].second.second]) {
                    on[ev[i][j].second.first][ev[i][j].second.second] = true;
                    us[ev[i][j].second.first][ev[i][j].second.second] = true;
                    ss[ev[i][j].second.first].insert({ev[i][j].first, ev[i][j].second.second});
                } else if (ev[i][j].first == -1 && on[ev[i][j].second.first][ev[i][j].second.second]) {
                    ss[ev[i][j].second.first].erase({i - 1, ev[i][j].second.second});
                }
            }
            bool ok = true;
            for (int j = 0; j < n; j++) {
                ok &= ss[j].size() != 0;
            }
            if (!ok) {
                continue;
            }
            for (int j = 0; j < n; j++) {
                pair <int, int> pp = *ss[j].begin();
                ss[j].erase(ss[j].begin());
                on[j][pp.second] = false;
            }
            i--;
            ans++;
        }
        printf("Case #%d: %d\n", t, ans);
    }

    return 0;

}
