#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>

using namespace std;

#define print(x) cout << x << endl
#define input(x) cin >> x

typedef long long llint;

const double pi = acos(-1.);

int main() {
    // freopen("a.txt", "r", stdin);
    int T;
    input(T);
    for (int case_ = 1; case_ <= T; case_++) {
        printf("Case #%d: ", case_);

        int n, k;
        input(n >> k);

        vector<pair<int, int> > ns;
        ns.resize(n);

        for (int i = 0; i < n; i++) {
            scanf("%d%d", &ns[i].first, &ns[i].second);
        }

        sort(ns.begin(), ns.end());
        multiset<llint> mp;
        for (auto item: ns) {
            mp.insert(1LL * item.second * item.first);
        }

        llint ans = 0;
        for (int i = n - 1; i >= 0; i--) {
            mp.erase(mp.find(1LL * ns[i].first * ns[i].second));
            llint cur = 1LL * ns[i].first * ns[i].first + 2LL * ns[i].first * ns[i].second;

            if (mp.size() < k - 1) {
                continue;
            }

            auto iter = mp.rbegin();
            for (int j = 0; j < k - 1; j++) {
                cur += 2LL * (*iter);
                ++iter;
            }

            ans = max(ans, cur);
        }
        printf("%.10lf\n", ans * pi);
    }
    return 0;
}
