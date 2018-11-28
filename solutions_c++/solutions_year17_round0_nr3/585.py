#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

const int LIMIT = 10000000;

unordered_map<long long, long long> memo;

long long f(long long n, long long threshold)
{
    if (n < threshold) {
        return 0;
    }
    if (memo.count(n)) {
        return memo[n];
    }
    long long mid = n + 1 >> 1;
    long long ret = f(mid - 1, threshold) + f(n - mid, threshold) + 1;
    memo[n] = ret;
    return ret;
}

int main()
{
    int tests, test = 1;
    for (scanf("%d", &tests); test <= tests; ++ test) {
        long long n, k;
        scanf("%I64d%I64d", &n, &k);

        long long l = 1, r = n + 1;
        while (l + 1 < r) {
            long long mid = l + r >> 1;
            memo.clear();
            if (f(n, mid) >= k) {
                l = mid;
            } else {
                r = mid;
            }
        }

        n = l;
        long long mid = n + 1 >> 1;
        long long left = mid - 1;
        long long right = n - mid;

        printf("Case #%d: %I64d %I64d\n", test, max(left, right), min(left, right));
    }
    return 0;
}
