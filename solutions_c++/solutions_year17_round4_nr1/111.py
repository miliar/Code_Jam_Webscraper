#include <cstdio>
#include <cassert>
#include <algorithm>
#include <iterator>
using namespace std;
int solve(int p, int c[4]) {
    if(p == 2) {
        return c[0] + (c[1] + 1) / 2;
    } else if(p == 3) {
        int x = min(c[1], c[2]);
        c[1] -= x;
        c[2] -= x;
        return c[0] + x + (c[1] + c[2] + 2) / 3;
    } else {
        return -1;
    }
}
int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        int n, p;
        scanf("%d %d", &n, &p);
        int c[4] = {};
        for(int j = 0; j < n; j++) {
            int x;
            scanf("%d", &x);
            c[x % p]++;
        }
        // printf("Case #%d:\n", i);
        // solve();
        printf("Case #%d: %d\n", i, solve(p, c));
    }
}
