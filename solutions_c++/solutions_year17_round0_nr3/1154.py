#include <cstdio>
#include <cstdlib>
#include <map>

using namespace std;

typedef long long ll;

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int ct = 1; ct <= T; ct++)
    {
        ll N, K;
        scanf("%lld%lld", &N, &K);
        //N = 1000000000000000000LL - rand()*rand();
        //K = 1000000000000000000LL - rand()*rand();

        map<ll, ll> lg;
        lg[N] = 1;

        while(lg.rbegin()->second < K)
        {
            ll val = lg.rbegin()->first, nb_fois = lg.rbegin()->second;
            K -= nb_fois;
            lg.erase(val);
            //printf("erased %lld\n", val);

            lg[val/2] += nb_fois;
            lg[(val-1)/2] += nb_fois;
        }

        ll act = lg.rbegin()->first;
        //printf("--> %lld\n", act);

        printf("Case #%d: %lld %lld\n", ct, act/2, (act-1)/2);
    }

    return 0;
}
