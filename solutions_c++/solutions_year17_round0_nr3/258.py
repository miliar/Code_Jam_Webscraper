#include <bits/stdc++.h>
using namespace std;

map<long long, long long> mp;
pair<long long, long long> calc(long long n, long long K) {
    mp.clear();
    mp[-n] = 1;
    while (true) {
        long long top = -(mp.begin()->first);
        long long num = (mp.begin()->second);
        if (num >= K) {
            return make_pair(top / 2, top - 1 - top / 2);
        } else {
            K -= num;
            mp.erase(mp.begin());
            mp[-(top / 2)] += num;
            mp[-(top - 1 - top / 2)] += num;
        }
    }
    return make_pair(-1, -1);
}


int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        long long n, K;
        scanf("%I64d%I64d", &n, &K);
        pair<long long, long long> res = calc(n, K);
        printf("Case #%d: %I64d %I64d\n", cas, res.first, res.second);
        cerr << res.first << " " << res.second << endl;
    }
    return 0;
}

