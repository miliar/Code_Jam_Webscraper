#include <cstdio>
#include <queue>

std::priority_queue<int> Q;
int main() {
    freopen("C-small-2-attempt1.in", "r", stdin);
    freopen("C-small-2-attempt1.out", "w", stdout);
    int T, N, K, I(1);
    scanf("%d", &T);
    while (T --> 0) {
        while (!Q.empty())
            Q.pop();
        scanf("%d%d", &N, &K);
        Q.push(N);
        while (K --> 0) {
            int s = Q.top(); Q.pop();
            int l = (s + 1) / 2 - 1, r = s / 2;
            if (l) Q.push(l);
            if (r) Q.push(r);
            if (!K) {
                printf("Case #%d: %d %d\n", I++, r, l);
            }
        }
    }
    return 0;
}
