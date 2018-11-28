#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>

using namespace std;

pair < long long, pair < int, int > > pan[1050];
int N, K;

//long long maax(int mask)
//{
//    int maxR = 0;
//    long long ret = 0;
//    for(int i = 0;i < N;++i)
//    {
//        if(mask & (1 << i))
//        {
//            maxR = max(maxR, pan[i].first);
//            ret += 2LL * pan[i].first * pan[i].second;
//        }
//    }
//    return ret += 1LL * maxR * maxR;
//}

int main()
{
        freopen("A-large.in", "r", stdin);
        freopen("out2.out", "w", stdout);
    int t, c = 0;
    scanf("%d", &t);
    while(t--)
    {
        ++c;
        scanf("%d%d", &N, &K);

        for(int i = 0;i < N;++i)
        {
            scanf("%d%d", &pan[i].second.first, &pan[i].second.second);
            pan[i].first = 1LL * pan[i].second.first * pan[i].second.second;
        }
        sort(pan, pan + N);

        long long maxR = 0;
        long long area = 0;
        for(int i = 0;i < K - 1;++i)
        {
            area += 2LL * pan[N - i - 1].first;
            maxR = max(maxR, 1LL * pan[N - i - 1].second.first);
        }

        long long z = 0;
        for(int i = K - 1;i < N;++i)
        {
            long long newR = pan[N - i - 1].second.first;
            long long x = newR * newR - maxR * maxR;

            if(x < 0)       x = 0;
            z = max(z, 2LL * pan[N - i - 1].first + x);

        }

        cerr << c << " <- done\n";
        area += z;
        printf("Case #%d: %.9f\n", c, 1.0 * (area + 1LL * maxR * maxR) * M_PI);
    }
    return 0;
}
