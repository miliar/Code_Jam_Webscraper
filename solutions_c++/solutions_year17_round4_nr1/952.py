#include <bits/stdc++.h>
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
using namespace std;

const int MAXN = 101 * 101 * 101 * 101;
struct state {
    int a, b, c, d, t;
};

bool operator<(const state& first, const state& second) {
    if(first.a != second.a)
        return first.a < second.a;
    if(first.b != second.b)
        return first.b < second.b;
    if(first.c != second.c)
        return first.c < second.c;
    if(first.d != second.d)
        return first.d < second.d;
    return first.t < second.t;
}
map<state, int> res;
int cnt[4];

void solve() {
    int n, p;
    scanf("%d%d", &n, &p);
    memset(cnt, 0, sizeof(cnt));
    for(int i = 0; i < n; i++) {
        int x;
        scanf("%d", &x);
        x %= p;
        cnt[x]++;
    }
    res.clear();
    res[{ 0, 0, 0, 0, 0 }] = 0;
    for(int a = 0; a <= cnt[0]; a++) {
        for(int b = 0; b <= cnt[1]; b++) {
            for(int c = 0; c <= cnt[2]; c++) {
                for(int d = 0; d <= cnt[3] && a + b + c + d <= n; d++) {
                    for(int r = 0; r < p; r++) {
                        if(res.find({ a, b, c, d, r }) == res.end()) continue;
                        if(res.find({ a + 1, b, c, d, (r + 0) % p }) == res.end())
                            res[{ a + 1, b, c, d, (r + 0) % p }] = res[{ a, b, c, d, r }] + (r > 0);
                        else
                            res[{ a + 1, b, c, d, (r + 0) % p }] = min(res[{ a + 1, b, c, d, (r + 0) % p }], res[{ a, b, c, d, r }] + (r > 0));

                        if(res.find({ a, b + 1, c, d, (r + 1) % p }) == res.end())
                            res[{ a, b + 1, c, d, (r + 1) % p }] = res[{ a, b, c, d, r }] + (r > 0);
                        else
                            res[{ a, b + 1, c, d, (r + 1) % p }] = min(res[{ a, b + 1, c, d, (r + 1) % p }], res[{ a, b, c, d, r }] + (r > 0));

                        if(res.find({ a, b, c + 1, d, (r + 2) % p }) == res.end())
                            res[{ a, b, c + 1, d, (r + 2) % p }] = res[{ a, b, c, d, r }] + (r > 0);
                        else
                            res[{ a, b, c + 1, d, (r + 2) % p }] = min(res[{ a, b, c + 1, d, (r + 2) % p }], res[{ a, b, c, d, r }] + (r > 0));

                        if(res.find({ a, b, c, d + 1, (r + 3) % p }) == res.end())
                            res[{ a, b, c, d + 1, (r + 3) % p }] = res[{ a, b, c, d, r }] + (r > 0);
                        else
                            res[{ a, b, c, d + 1, (r + 3) % p }] = min(res[{ a, b, c, d + 1, (r + 3) % p }], res[{ a, b, c, d, r }] + (r > 0));
                    }
                }
            }
        }
    }
    int ans = 1e9;
    for(int r = 0; r < p; r++) {
        if(res.find({ cnt[0], cnt[1], cnt[2], cnt[3], r }) == res.end()) continue;
        ans = min(ans, res[{ cnt[0], cnt[1], cnt[2], cnt[3], r }]);
    }
    printf("%d\n", n - ans);
}

int main() {
    //ios_base::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        solve();
    }
    return 0;
}