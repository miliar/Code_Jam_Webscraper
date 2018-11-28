#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

long long n, k;

long long mii(long long x, int level)
{
    for(int i = 0;i < level;++i)
        x = (x - 1) >> 1;

    return x;
}

long long maa(long long x, int level)
{
    return x >> level;
}

void print(long long x)
{
    long long mi = (x - 1) / 2;
    long long ma = x >> 1;
    printf("%lld %lld\n", ma, mi);
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t, c = 0;
    scanf("%d", &t);
    while(t--)
    {
        ++c;
        scanf("%lld%lld", &n, &k);
        printf("Case #%d: ", c);

        long long cnt = 0;
        int z = 0;
        while(true)
        {
            cnt += (1LL << z);
            if(cnt >= k)
            {
                cnt -= (1LL << z);

                long long i = n & ((1LL << z) - 1);
                ++i;
                if(cnt + i >= k)
                    print(maa(n, z));
                else
                    print(mii(n, z));
                break;
            }
            ++z;
        }
    }
    return 0;
}
