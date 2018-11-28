#include <bits/stdc++.h>

using namespace std;
int cases = 1;

int main(void) {
    freopen("/home/vanessi/CLionProjects/CodeJam2017QC/C-small-2-attempt0.in", "r", stdin);
    freopen("/home/vanessi/CLionProjects/CodeJam2017QC/C-small-2-attempt0.out", "w", stdout);
    int testcases;
    scanf("%d", &testcases);
    while (testcases--) {
        long long N;
        int K;
        priority_queue<long long> next;
        scanf("%lld %d", &N, &K);
        long long s = N, e = N;
        next.push(N);
        while (K--) {
            long long ns = (next.top()) / 2, ne = ((next.top()) / 2 + (next.top()) % 2) - 1;
            next.pop();
            next.push(ns);
            next.push(ne);
            s = ns, e = ne;
        }
        printf("Case #%d: %lld %lld\n", cases++, max(s, 0LL), max(e, 0LL));
    }
}