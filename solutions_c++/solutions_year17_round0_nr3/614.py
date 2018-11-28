#include <cstdio>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <functional>
#include <map>
using namespace std;
static_assert(sizeof(long) == 8);
long solve(long n, long k) {
    map<long, long, greater<long>> q;
    q[n] = 1;
    k--;
    while(k) {
        long x = q.begin()->first;
        long y = min(q.begin()->second, k);
        q.begin()->second -= y;
        k -= y;
        q[x / 2] += y;
        q[(x - 1) / 2] += y;
        if(q.begin()->second == 0)
            q.erase(q.begin());
    }
    return q.begin()->first;
}
int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        long n, k;
        scanf("%ld %ld", &n, &k);
        long y = solve(n, k);
        printf("Case #%d: %ld %ld\n", i, y / 2, (y - 1) / 2);
    }
}
