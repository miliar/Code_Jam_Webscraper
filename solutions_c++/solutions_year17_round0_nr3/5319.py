#include <bits/stdc++.h>
using namespace std;
 
int kases, n, k;
 
int main(){
    #ifdef ULTMASTER
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    #endif
    scanf("%d", &kases);
    for (int kase = 1; kase <= kases; ++kase) {
        scanf("%d%d", &n, &k);
        priority_queue<int> q;
        q.push(n);
        int m, M;
        for (int i = 0; i < k; ++i) {
            int t = q.top(); q.pop();
            m = (t - 1) / 2;
            M = t - 1 - m;
            q.push(m);
            q.push(M);
        }
        printf("Case #%d: %d %d\n", kase, M, m);
    }
    return 0;
}