#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ll;

map<ll, ll> ss;


int main()
{
    int T;
    scanf("%d", &T);
    for (int c=1; c<=T; c++)
    {
        ll NN, K;
        scanf("%llu %llu", &NN, &K);

        ss.clear();

        ss[ NN ] = 1;

        printf("Case #%d: ", c);
        for (;K>0;)
        {
            auto it = --ss.end();
            ll N = (*it).first;
            ll cnt = (*it).second;
            ll tmp = (N+1)/2;
            ss.erase(it);

            if (cnt >= K)
            {
                printf("%llu %llu", N - tmp, tmp - 1);
                break;
            }

            K -= cnt;
            ss[tmp - 1] += cnt;
            ss[N - tmp] += cnt;

        }
        printf("\n");
    }

    return 0;
}

