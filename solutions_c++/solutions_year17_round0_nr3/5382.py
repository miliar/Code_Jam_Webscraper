#include <cstdio>
#include <cstring>
#include <queue>
#include <vector>
#include <map>


#pragma warning(disable:4996)

using namespace std;

int main() {
    freopen("stall.in", "r", stdin);
    freopen("stall.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        long long n;
        long long k;

        scanf("%lld %lld", &n, &k);

        // dist -> count
        map<long long, long long> intervals;
        intervals[n] = 1;

        priority_queue<long long> Q;
        Q.push(n);

        long long ans_high;
        long long ans_low;

        long long i = 0;
        while (i < k) {
            long long top = Q.top();
            long long amount = min(intervals[top], k - i);
            intervals[top] -= amount;
            if (intervals[top] == 0) { Q.pop(); }
            long long low = (top - 1) / 2;
            long long high = top / 2;
            ans_high = high;
            ans_low = low;
            if (intervals.find(low) == intervals.end() || intervals[low] == 0) {
                Q.push(low);
            }
            if (intervals.find(high) == intervals.end() || intervals[high] == 0) {
                Q.push(high);
            }

            intervals[low] += amount;
            intervals[high] += amount;

            i += amount;
        }

        
        printf("Case #%d: %lld %lld\n", t, ans_high, ans_low);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}