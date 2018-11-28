#include <cstdio>
#include <map>
#include <assert.h>

using namespace std;

pair<long long, long long> solve(long long n, long long k) {
    map<long long, long long> buckets;
    buckets[n] = 1;
    long long used = 0;
    long long last_bucket = -1;
    while (used < k) {
        pair<long long, long long> bucket = *buckets.rbegin();
        long long size = bucket.first, count = bucket.second;
        assert(size != 0);
        if (size & 1) {
            buckets[size / 2] += count * 2;
        } else {
            buckets[size / 2] += count;
            buckets[size / 2 - 1] += count;
        }
        used += count;
        last_bucket = size;
        buckets.erase(buckets.find(size));
    }
    return {last_bucket / 2, last_bucket / 2 - ((last_bucket & 1) ^ 1)};
}

int main() {
    int t;
    scanf("%d", &t);
    for (int c = 0; c < t; c++) {
        long long n, k;
        scanf("%lld %lld", &n, &k);
        auto result = solve(n, k);
        printf("Case #%d: %lld %lld\n", c + 1, result.first, result.second);
    }
    return 0;
}