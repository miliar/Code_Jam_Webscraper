#include <bits/stdc++.h>
using namespace std;

int main() {
    int T; scanf("%d", &T);
    for (int test = 1; test <= T; test++) {
        int N, K;
        scanf("%d %d", &N, &K);

        priority_queue<long long> Q;

        Q.push(N);
        long long x;
        for (int i = 0; i < K - 1; i++) {
            x = Q.top();
            Q.pop();
                       
            if (x % 2 == 0) {
                if (x/2 - 1 > 0) Q.push(x/2 - 1);
                if (x - x/2 > 0) Q.push(x - x/2);
            } else {
                if (x/2 > 0) {
                    Q.push(x/2);
                    Q.push(x/2);
                }
            }
        }
        x = Q.top();
        long long mini, maxi;
        if (x % 2 == 0) {
            maxi = x/2;
            mini = x/2 - 1;
        } else {
            mini = maxi = x/2;
        }

        printf("Case #%d: %lld %lld\n", test, maxi, mini);
    }
}
