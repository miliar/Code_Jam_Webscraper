#include <bits/stdc++.h>
using namespace std;

map <long long, long long> cnt;
priority_queue <long long> pq;
long long tmp, n, k;
long long last, l, r;

int main() {
    int TC;
    scanf("%d", &TC);
    for (int zz = 1; zz <= TC; zz++) {
        cnt.clear();
        tmp = 0;
        
        scanf("%lld %lld", &n, &k);
        pq.push(n);
        cnt[n] = 1;
        while (tmp < k) {
            long long now = pq.top();
            pq.pop();

            // printf("%lld %lld\n", now, cnt[now]);
            last = now;
            tmp += cnt[now];

            l = now/2;
            r = now/2 - (now%2==0);

            if (l > 0) {
                if (cnt[l] == 0)
                    pq.push(l);
                cnt[l] += cnt[now];
            }
            if (r > 0) {
                if (cnt[r] == 0)
                    pq.push(r);
                cnt[r] += cnt[now];
            }

            cnt.erase(now);
        }
        printf("Case #%d: ", zz);
        printf("%lld %lld\n", l, r);
    }
}