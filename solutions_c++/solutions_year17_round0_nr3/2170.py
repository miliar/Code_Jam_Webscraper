#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

void solve(int nt) {
    LL n, k;
    scanf("%lld%lld", &n, &k);
    printf("Case #%d: ", nt);

    map<LL,LL> mp;
    mp[n+1]++;
    k--;
    while (k) {
        auto it = mp.end();
        --it;
        LL tmp = it->first;
        LL cnt = it->second;

        if (k >= cnt) {
            k -= cnt;
            mp.erase(it);
            mp[tmp/2] += cnt;
            mp[(tmp+1)/2] += cnt;
        }
        else {
            it->second -= k;
            mp[tmp/2] += k;
            mp[(tmp+1)/2] += k;
            k = 0;
        }
    }

    auto ite = mp.end();
    --ite;

    printf("%lld %lld\n", (ite->first+1)/2-1, (ite->first)/2-1);
}

int main() {
    int ct;
    scanf("%d", &ct);
    for (int nt = 1; nt <= ct; nt++) {
        solve(nt);
        fprintf(stderr, "Case %d done.\n", nt);
    }
}
