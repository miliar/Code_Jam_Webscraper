#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>

#include <map>

using namespace std;

long long N, K;

map <long long, long long> bathroom;

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int Cas = 1; Cas <= T; ++Cas) {
        bathroom.clear();

        scanf("%lld %lld", &N, &K);

        bathroom[N] = 1;
        while (K > 0) {
            auto m = bathroom.end();
            m--;

            long long len = m->first;
            long long cnt = m->second;

            bathroom[len / 2ll] += cnt;
            bathroom[(len - 1ll) / 2ll] += cnt;

            K -= cnt;
            bathroom.erase(m);

            if (K <= 0) {
                printf("Case #%d: %lld %lld\n", Cas, len / 2ll, (len - 1ll) / 2ll);
                break;
            }
        }
    }

    return 0;
}
