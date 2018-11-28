#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n, r, o, y, g, b, v;
        scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
        pair<int, char> a[3] = {{r, 'R'}, {y, 'Y'}, {b, 'B'}};
        sort(a, a + 3);
        if (a[2].first > a[0].first + a[1].first) {
            printf("Case #%d: IMPOSSIBLE\n", cas);
            fprintf(stderr, "Case #%d: IMPOSSIBLE\n", cas);
        } else {
            string res = "";
            while (a[0].first + a[1].first + a[2].first > 0) {
                if (a[2].first > 0) {
                    res += a[2].second;
                    a[2].first--;
                }
                if (a[1].first > 0 && a[1].first >= a[0].first) {
                    res += a[1].second;
                    a[1].first--;
                } else if (a[0].first > 0) {
                    res += a[0].second;
                    a[0].first--;
                }
            }
            printf("Case #%d: %s\n", cas, res.c_str());
            fprintf(stderr, "Case #%d: %s\n", cas, res.c_str());
        }
    }
}