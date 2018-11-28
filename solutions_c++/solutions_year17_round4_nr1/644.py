#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int n, p, a[105], g[105];
map<pair<vector<int>, int>, int> dp;
void load() {
    cin >> n >> p;
    memset(a, 0, sizeof(a));
    for (int i = 0;i < n;i++) {
        cin >> g[i];
        a[g[i] % p] += 1;
    }
}

int go(vector<int> b, int left) {
    if (dp.find(make_pair(b, left)) != dp.end()) return dp[make_pair(b, left)];
    int res = 0;

    for (int i = 1;i < p;i++) {
        if (b[i] > 0) {
            b[i]--;
            int t = go(b, (left - i + p) % p) + (left == 0);
            b[i]++;
            res = max(res, t);
        }
    }
    dp[make_pair(b, left)] = res;
    return res;
}

void solve(int test) {
    printf("Case #%d: ", test);
    dp.clear();
    int ans = a[0];
    vector<int> b;
    b.push_back(0);
    for (int i = 1;i < p;i++) {
        b.push_back(a[i]);
    }
    ans += go(b, 0);
    printf("%d\n", ans);
}

int main() {
#ifdef VALERA
    freopen("a.in", "r", stdin);
#endif
    int t;
    cin >> t;

    for (int i = 0;i < t;i++) {
        load();
        solve(i + 1);
    }
    return 0;
}
