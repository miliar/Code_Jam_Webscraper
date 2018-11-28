#include <vector>
#include <stdio.h>
#include <algorithm>
#include <queue>
#include <utility>

int solve(int t) {
    long long n,k;
    std::priority_queue<long long> pq;
    scanf("%lld%lld", &n, &k);
    pq.push(n);
    long long y, z;
    for (int i = 0;  i!= k; ++i) {
        auto pr = pq.top(); pq.pop();
        if (pr%2 ==0) {
            pq.push(pr/2);
            y = pr/2;
            pq.push(pr/2 - 1);
            z = pr/2 - 1;
        } else{
          pq.push(pr/2);
          pq.push(pr/2);
          y = pr/2;
          z = pr/2;
        }
    }
   printf("Case #%d: %lld %lld\n", t+1, y, z);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 0; i != T; ++i) {
        solve(i);
    }
    return 0;
}
