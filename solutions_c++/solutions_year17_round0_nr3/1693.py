#include <cstdio>
#include <map>

typedef std::map<long long, long long, std::greater<long long> > Map;

void solve(void)
{
    Map m;
    Map::iterator i;
    long long n, k, d, l, r;

    scanf("%lld%lld", &n, &k);

    m[n] = 1;

    while (k > 0) {
        i = m.begin();
        d = i->first;
        n = i->second;
        l = (d - 1) / 2;
        r = d / 2;
        m.erase(i);
        m[l] += n;
        m[r] += n;
        k -= n;
    }

    printf("%lld %lld\n", r, l);
}

int main(void)
{
    int i, t;

    scanf("%d", &t);

    for (i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        solve();
    }

    return 0;
}
