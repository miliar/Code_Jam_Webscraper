#include <cstdio>
#include <queue>

unsigned long long max(unsigned long long a, unsigned long long b) {
    return a > b ? a : b;
}

unsigned long long min(unsigned long long a, unsigned long long b) {
    return a < b ? a : b;
}

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        unsigned long long n, k;
        scanf("%llu %llu", &n, &k);
        std::priority_queue<unsigned long long> fringe;
        fringe.push(n);
        unsigned long long l = 0;
        while (true) {
            unsigned long long stalls = fringe.top();
            fringe.pop();
            l++;
            unsigned long long left = stalls / 2;
            unsigned long long right = stalls - left - 1;

            if (l == k) {
                printf("Case #%d: %llu %llu\n", i, max(left, right), min(left, right));
                break;
            } else {
                fringe.push(left);
                fringe.push(right);
            }
        }
    }
    return 0;
}
