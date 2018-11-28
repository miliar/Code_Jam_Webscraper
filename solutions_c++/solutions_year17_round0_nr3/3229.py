#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <queue>
#include <map>
#include <vector>
#define fi first
#define se second
using namespace std;
typedef long long llint;
typedef pair<int, int> pii;

map<llint, llint, greater<llint> > mp;

int main() {
    // Self-Judge.
    //    freopen("/Users/Clair/Desktop/C-large.in", "r", stdin);
    //    freopen("/Users/Clair/Desktop/C-large-out.txt", "w+", stdout);
    int t;
    scanf("%d", &t);
    for (int tt = 1; tt <= t; tt++) {
        llint n, k;
        scanf("%lld%lld", &n, &k);
        mp.clear();
        mp[n] = 1;
        llint ans1 = 0, ans2 = 0, sum = 0;
        while (sum < k) {
            auto it = mp.begin();
            mp[it->fi/2] += it->se;
            mp[it->fi/2-(it->fi % 2 == 0)] += it->se;
            sum += it->se;
            if (sum >= k) {
                ans1 = it->fi/2-(it->fi % 2 == 0), ans2 = it->fi/2;
            }
            mp.erase(it);
        }
        printf("Case #%d: %lld %lld\n", tt, max(ans1, ans2), min(ans1, ans2));
    }
}
