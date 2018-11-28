#include <cstdio>
#include <cassert>
#include <map>
using namespace std;

typedef long long llong;

void solve(int cs) {
    llong n, k;
    scanf("%lld %lld", &n, &k);
    map<pair<llong, llong>, llong> cnt = {{{(n - 1) / 2, n / 2}, 1}};
    pair<llong, llong> ans(-1, -1);
    while (true) {
        assert(cnt.size() <= 2);
        assert(!cnt.empty());
        llong tot = 0;
        for (const auto& pr : cnt)
            tot += pr.second;
        if (k <= tot) {
            if (cnt.rbegin()->second >= k) {
                ans = cnt.rbegin()->first;
            } else {
                assert(cnt.size() == 2);
                ans = cnt.begin()->first;
            }
            break;
        }
        k -= tot;
        decltype(cnt) ncnt;
        for (const auto& pr : cnt) {
            if (pr.first.first)
                ncnt[make_pair((pr.first.first - 1) / 2, pr.first.first / 2)] += pr.second;
            if (pr.first.second)
            ncnt[make_pair((pr.first.second - 1) / 2, pr.first.second / 2)] += pr.second;
        }
        cnt.swap(ncnt);
    }
    assert(ans.first != -1);
    printf("Case #%d: %lld %lld\n", cs, ans.second, ans.first);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        solve(i + 1);
        fprintf(stderr, "%d\n", i);
        fflush(stdout);
    }
}
