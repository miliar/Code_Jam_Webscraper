#include <stdio.h>
#include <map>

int main()
{
    int cas;
    scanf("%d", &cas);
    for (int ca = 1; ca <= cas; ++ ca) {
        long long n, K;
        scanf("%lld%lld", &n, &K);
        std::map<long long, long long> cnt;
        cnt[n] = 1;
        long long last;
        while (K) {
            long long x, y;
            std::tie(x, y) = *cnt.rbegin();
            cnt.erase(std::next(cnt.rbegin()).base());
            last = x;
            long long w = std::min(K, y);
            K -= w;
            y -= w;
            if (y) cnt[x] += y;
            cnt[x - 1 - (x - 1 >> 1)] += w;
            cnt[x - 1 >> 1] += w;
        }
        printf("Case #%d: %lld %lld\n", ca, last - 1 - (last - 1 >> 1), last - 1 >> 1);
    }
}
