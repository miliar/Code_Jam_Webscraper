#include <bits/stdc++.h>
#define sz(x) (int((x).size()))
#define pb push_back
#define eb emplace_back
#define all(x) (x).begin(), (x).end()
template<typename T> bool domax(T &a, T b) { return (b > a ? (a = b, true) : false); }
template<typename T> bool domin(T &a, T b) { return (b < a ? (a = b, true) : false); }
typedef long long ll;

const int maxn = 105;

int n, p, c[4];

int main() {
    int Testcases;
    scanf("%d", &Testcases);
    for (int testcase = 1; testcase <= Testcases; testcase++) {
        scanf("%d%d", &n, &p);
        c[0] = c[1] = c[2] = c[3] = 0;
        for (int i = 0; i < n; i++) {
            int g;
            scanf("%d", &g);
            c[g%p]++;
        }
        int ans = 0;
        if (p == 2) {
            ans += c[0];
            ans += (c[1] + 1) / 2;
        } else if (p == 3) {
            ans += c[0];
            int k = std::min(c[1], c[2]);
            ans += k;
            c[1] -= k;
            c[2] -= k;
            ans += (c[1] + 2) / 3 + (c[2] + 2) / 3;
        } else {
            ans += c[0];
            {
                int k = c[2] / 2;
                ans += k;
                c[2] -= k * 2;
            }
            {
                int k = std::min(c[1], c[3]);
                ans += k;
                c[1] -= k;
                c[3] -= k;
            }
            int mod = 0;
            if (c[2]) {
                assert(c[2] == 1);
                ans++;
                mod += 2;
            }
            while (c[1]) {
                if (mod == 0) ans++;
                mod = (mod + 1) % p;
                c[1]--;
            }
            while (c[3]) {
                if (mod == 0) ans++;
                mod = (mod + 3) % p;
                c[3]--;
            }
        }
        printf("Case #%d: %d\n", testcase, ans);
    }
}

