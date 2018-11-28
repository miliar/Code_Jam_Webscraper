#include <stdio.h>
#include <queue>

int main()
{
    int t;
    scanf("%d", &t);
    for (int cases = 1; cases <= t; cases++) {
        uint64_t n;
        scanf("%llu", &n);
        std::deque<int> q;
        while (n) {
            q.push_front(n % 10);
            n /= 10;
        }
        for (int i = 1; i < q.size(); i++) {
            if (q[i] < q[i - 1]) {
                for (int j = i - 1; j >= 0; j--) {
                    q[j]--;
                    if (!j || q[j] >= q[j - 1]) {
                        break;
                    }
                    q[j] = 9;
                }
                for (int j = i; j < q.size(); j++) {
                    q[j] = 9;
                }
                break;
            }
        }
        for (auto digit : q) {
            n = n * 10 + digit;
        }
        printf("Case #%d: %llu\n", cases, n);
    }
    return 0;
}
