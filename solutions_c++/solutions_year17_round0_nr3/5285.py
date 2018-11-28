#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;

ull calcGroup(ull k)
{
    int x = 63;
    while((k >> x) != ull(1)) --x;
    return x;
}

pair<ull, ull> getRes(int gidx)
{
    if(gidx == 1) return make_pair(0, 0);
    else {
        ull u1 = gidx / 2;
        ull u2;
        if(gidx % 2 == 0) u2 = u1 - 1;
        else u2 = u1;
        return make_pair(u1, u2);
    }
}

int main()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0.out","w",stdout);
    int t;
    scanf("%d", &t);
    ull n, k;
    for(int i = 0; i != t; ++i) {
        scanf("%llu %llu", &n, &k);
        ull grouplen = (ull)1 << calcGroup(k);
        ull gidx = (n - k + 1) / grouplen;
        if((n - k + 1) % grouplen != 0) ++gidx;
        auto res = getRes(gidx);
        printf("Case #%d: %llu %llu\n", i + 1, res.first, res.second);
    }
    return 0;
}
