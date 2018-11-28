#include <stdio.h>
#include <set>
#include <map>
#include <assert.h>

#define DEBUG false

using namespace std;

typedef long long int ll;

int T;
ll n, k;
set <ll, greater<ll> > sizes;
map <ll, ll> gaps;

int main () {
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ", i);
        scanf("%lld %lld", &n, &k);
        sizes.clear();
        gaps.clear();
        assert(sizes.empty() && gaps.empty());
        gaps[n] = 1LL;
        sizes.insert(n);
        while (1) {
            ll max_gap = *(sizes.begin());
            ll times = gaps[max_gap];
            if ( DEBUG ) printf("\nmax %lld times %lld\n", max_gap, times);
            sizes.erase(sizes.begin());
            gaps.erase(max_gap);
            if (k <= times)
            {
                printf("%lld %lld\n", max_gap / 2LL, ( max_gap - 1LL ) / 2LL);
                break;
            }
            else
            {
                k -= times;
                ll M = max_gap / 2LL, m = (max_gap - 1LL) / 2LL;
                if ( gaps.find(M) != gaps.end() )
                {
                    gaps[M] += times;
                }
                else
                {
                    gaps[M] = times;
                    sizes.insert(M);
                }

                if (gaps.find(m) != gaps.end())
                {
                    gaps[m] += times;
                }
                else
                {
                    gaps[m] = times;
                    sizes.insert(m);
                }
            }
        }
    }
    return 0;
}