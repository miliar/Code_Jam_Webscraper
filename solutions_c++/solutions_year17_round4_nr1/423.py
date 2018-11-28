#include <bits/stdc++.h>

using namespace std;

#define fi first
#define se second
#define pb push_back

const int N = 5;
unordered_map<int, int> m;
int a[N];
int kol[N];

int hashc(int p) {
    int x = 0;
    for (int i = 1; i < p; ++i) {
        x = (x * 4733 + a[i]) % 1000000007;
    }
    return x;
}

int solve(int p) {
    bool flag = false;
    for (int i = 1; i < p; ++i) {
        if (a[i] != 0) {
            flag = true;
        }
    }
    if (!flag) {
        return 0;
    }
    int code = hashc(p);
    if (m.count(code)) {
        return m[code];
    }
    int ans = 1;
    for (int i = 1; i < p; ++i) {
        if (a[i] >= kol[i]) {
            a[i] -= kol[i];
            ans = max(ans, solve(p) + 1);
            a[i] += kol[i];
        }
    }
    for (int on = 0; on < kol[1]; ++on) {
        for (int tw = 0; tw < kol[2]; ++tw) {
            for (int th = 0; th < kol[3]; ++th) {
                if (on + tw + th > 0 && (on + tw * 2 + th * 3) % p == 0
                    && a[1] >= on && a[2] >= tw && a[3] >= th) {
                    a[1] -= on;
                    a[2] -= tw;
                    a[3] -= th;
                    ans = max(ans, solve(p) + 1);
                    a[1] += on;
                    a[2] += tw;
                    a[3] += th;
                }
            }
        }
    }
    return m[code] = ans;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int tt = 1; tt <= t; ++tt) {
        int n, p;
        scanf("%d%d", &n, &p);
        fill(a, a + N, 0);
        for (int i = 1; i <= n; ++i) {
            int x;
            scanf("%d", &x);
            a[x % p]++;
        }
        fill(kol, kol + N, 1);
        for (int i = 1; i < p; ++i) {
            kol[i] = p / __gcd(i, p);
        }
        int ans = a[0];
        m.clear();
        ans += solve(p);
        printf("Case #%d: %d\n", tt, ans);
    }
}
