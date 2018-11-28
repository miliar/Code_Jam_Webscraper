#include <cstdio>
#include <map>

using namespace std;

typedef long long ll;

int main()
{
    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; ++t) {

        ll n, k;
        scanf("%lld%lld", &n, &k);

        map<ll, ll> count;
        count[n] = 1;

        ll x = 0;
        for (auto it = count.rbegin(); it != count.rend(); ++it)
        {
            ll ix = it->first;
            ll c = it->second;

            ll div1 = ix / 2;
            ll div2 = div1;
            if (ix % 2 == 0 && div2 > 0)
                --div2;
            
            x += c;
            if (x >= k) {
                printf("Case #%d: %lld %lld\n", t, div1, div2);
                break;
            }

            count[div1] += c;
            count[div2] += c;
        }

    }

    return 0;
}