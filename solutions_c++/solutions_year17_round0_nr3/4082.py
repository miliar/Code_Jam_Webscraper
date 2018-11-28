#include <stdio.h>
#include <queue>
using namespace std;

typedef long long ll;
ll N, K;

struct intervallo_t {
    ll s, e;
    bool operator< (const intervallo_t& t) const {
        if ((e-s) == (t.e - t.s)) return (s > t.s);
        return (e-s) < (t.e - t.s);
    }
};

int main() {
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T, count = 0;
    scanf("%d", &T);
    while (T-- > 0) {
        priority_queue<intervallo_t> intervalli;
        scanf("%lld%lld", &N, &K);
        intervalli.push({1, N});
        ll r_max, r_min;
        for (ll i = 0; i < K; i++) {
            ll chosen;
            intervallo_t itv = intervalli.top();
            intervalli.pop();
            ll diff = (itv.e - itv.s);
            chosen = itv.s + diff/2;
            if (chosen-1 >= itv.s) {
                //printf("Aggiungo %lld, %lld\n", itv.s, chosen-1);
                intervalli.push({itv.s, chosen-1});
            }
            if (chosen+1 <= itv.e) {
                //printf("Aggiungo %lld, %lld\n", chosen+1, itv.e);
                intervalli.push({chosen+1, itv.e});
            }

            ll d1 = (chosen-1) - itv.s + 1;
            ll d2 = itv.e - (chosen+1) + 1;
            //printf("(%d, %d)\n", d1, d2);
            if (d1 > d2) {
                r_max = d1;
                r_min = d2;
            }
            else {
                r_max = d2;
                r_min = d1;
            }

            //printf("Divido intervallo %lld, %lld in [%lld] (%lld, %lld) e (%lld, %lld)\n", itv.s, itv.e, chosen, itv.s, chosen-1, chosen+1, itv.e);
        }

        printf("Case #%d: %lld %lld\n", ++count, r_max, r_min);

        //printf("%d, %d\n", intervalli.top().s, intervalli.top().e);
    }
}
