#include <bits/stdc++.h>
using namespace std;

#define MAX 1001
#define MOD 12345

main() {
    #ifdef LOCAL_BUILD
        freopen("1.in", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    ios::sync_with_stdio(0);

    int t;
    cin >> t;
    for (int t1 = 1; t1 <= t; ++t1) {
        multiset<long long, greater<long long> > s;
        long long n, k;
        cin >> n >> k;

        s.insert(n);
        for (int i = 0; i < k-1; ++i) {
            long long t = *s.begin();
            s.erase(s.begin());

            if (t == 1)
                break;

            long long t1 = max(0LL, (t-1)/2), t2 = max(0LL, t-1-t1);
            //printf("%lld -> %lld %lld\n", t, t1, t2);
            if (t1)
                s.insert(t1);
            if (t2)
                s.insert(t2);
        }

        long long t = *s.begin();
        printf("Case #%d: %lld %lld\n", t1, t/2, (t-1)/2);

        /*long long n, k;
        cin >> n >> k;
        int h = 0;
        long long tmp = 2;
        while (tmp-1 < k) {
            h++;
            tmp *= 2;
        }

        tmp = n;
        for (int i = 0; i < h; ++i) {
            tmp /= 2;
        }

        printf("Case #%d: %lld %lld\n", t1, tmp/2, (tmp-1)/2);*/
    }

    return 0;
}
