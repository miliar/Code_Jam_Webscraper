#include <cstdio>
#include <cassert>
#include <algorithm>
#include <iterator>
#include <numeric>
using namespace std;
int p[1000], b[1000];
int cp[1000], cb[1000], scp[1000];
int gety(int n, int c, int m) {
    fill_n(cp, n, 0);
    fill_n(cb, c, 0);
    for(int i = 0; i < m; i++)
        cp[p[i]]++, cb[b[i]]++;
    int ans = *max_element(cb, cb + c);
    partial_sum(cp, cp + n, scp);
    for(int i = 0; i < n; i++)
        ans = max(ans, (scp[i] + i) / (i + 1));
    return ans;
}
int getz(int n, int c, int m, int y) {
    int z = 0;
    for(int i = n - 1; i >= 0; i--)
        if(cp[i] > y)
            z += cp[i] - y;
    return z;
}
int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        int n, c, m;
        scanf("%d %d %d", &n, &c, &m);
        for(int j = 0; j < m; j++)
            scanf("%d %d", p + j, b + j), p[j]--, b[j]--;
        // printf("Case #%d:\n", i);
        // solve();
        int y = gety(n, c, m);
        int z = getz(n, c, m, y);
        printf("Case #%d: %d %d\n", i, y, z);
    }
}
