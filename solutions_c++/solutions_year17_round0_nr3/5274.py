#include <queue>
#include <algorithm>
#include <cstdio>
#include <iostream>
using namespace std;

typedef unsigned long long ull;

int t;
ull n, k;

int main() {
    cin >> t;
    for(int tc = 1; tc <= t; ++tc) {
        cin >> n >> k;
        priority_queue<ull> pq;
        pq.push(n);
        for(ull i = 0; i < k-1; ++i) {
            ull top = pq.top(); pq.pop();
            ull big = top/2;
            pq.push(big);
            ull small = (top-1)/2;
            pq.push(small);
        }
        ull top = pq.top();
        ull big = top/2;
        ull small = (top-1)/2;

        printf("Case #%d: %llu %llu\n", tc, big, small);
    }

    return 0;
}
