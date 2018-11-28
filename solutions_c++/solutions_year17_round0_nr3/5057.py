#include <bits/stdc++.h>

using namespace std;

int main (void) {
    int t;
    scanf ("%d", &t);
    for (int c = 1; c <= t; c++) {
        int n, k;
        priority_queue<int> pq;
        scanf ("%d%d", &n, &k);
        pq.push(n);
        for (int i = 1; i < k; i++) {
            n = pq.top(); pq.pop();
            pq.push(n/2);
            pq.push((n-1)/2);
        }
        n = pq.top();
        printf ("Case #%d: %d %d\n", c, n/2, (n-1)/2);
    }
}
