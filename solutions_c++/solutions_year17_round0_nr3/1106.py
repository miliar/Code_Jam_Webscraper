#include <cstdio>
#include <queue>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        long long n, k;
        scanf("%lld%lld", &n, &k);
        priority_queue<long long> q;
        q.push(n);
        for (int i = 0; i < k - 1; i++) {
            long long w = q.top() - 1; q.pop();
            q.push(w / 2);
            q.push(w - w / 2);
        }
        long long w = q.top() - 1;
        printf("Case #%d: %lld %lld\n", t, w - w / 2, w / 2);
    }
    return 0;
}
