#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int maxn = 222;

struct event {
    int s, t, w;
}a[maxn];

bool cmp(const event& e1, const event& e2) {
    return e1.s < e2.s;
}

int main() {
    freopen("bl.txt", "r", stdin);
    freopen("blout.txt", "w", stdout);
    int T, ca = 0;
    cin >> T;
    while (T--) {
        int n, m;
        cin >> n >> m;
        for (int i = 1; i <= n; ++i) {
            cin >> a[i].s >> a[i].t;
            a[i].w = 0;
        }
        for (int i = n + 1; i <= n + m; ++i) {
            cin >> a[i].s >> a[i].t;
            a[i].w = 1;
        }
        sort(a + 1, a + 1 + n + m, cmp);
        int val0 = 720, val1 = 720;
        for (int i = 1; i <= n + m; ++i) {
            int w = a[i].w, s = a[i].s, t = a[i].t;
            if (w == 0) {
                val0 -= t - s;
            } else {
                val1 -= t - s;
            }
        }
        a[0] = a[n + m];
        a[0].s -= 1440;
        a[0].t -= 1440;
        int ans = 0;
        vector<int> vec0, vec1;
        for (int i = 1; i <= n + m; ++i) {
            if (a[i].w != a[i - 1].w) ans++;
            int w = a[i].w;
            if (a[i].w == a[i - 1].w) {
                if (w == 0) {
                    vec0.push_back(a[i].s - a[i - 1].t);
                } else {
                    vec1.push_back(a[i].s - a[i - 1].t);
                }
            }
        }
        sort(vec0.begin(), vec0.end());
        sort(vec1.begin(), vec1.end());
        for (int i = 0; i < vec0.size(); ++i) {
            if (vec0[i] <= val0) {
                val0 -= vec0[i];
            } else {
                ans += 2;
            }
        }
        for (int i = 0; i < vec1.size(); ++i) {
            if (vec1[i] <= val1) {
                val1 -= vec1[i];
            } else {
                ans += 2;
            }
        }
        printf("Case #%d: %d\n", ++ca, ans);
        
    }
    return 0;
}
