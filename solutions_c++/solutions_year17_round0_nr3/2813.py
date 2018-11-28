#pragma warning(disable:4996)
#include <stdio.h>
#include <map>

long long n, k;

std::map<long long, long long> m;

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    int t, tt=0;
    scanf("%d", &t);

    while(t--)
    {
        scanf("%lld%lld", &n, &k);

        m.clear();
        m[n] = 1;

        printf("Case #%d: ", ++tt);

        while (true)
        {
            std::map<long long, long long>::reverse_iterator it = m.rbegin();

            long long s = it->first;
            long long c = it->second;

            long long l = (s-1) / 2;
            long long r = s / 2;

            if (k <= c)
            {
                printf("%lld %lld\n", r, l);
                break;
            }

            k -= c;

            m[l] += c;
            m[r] += c;

            m.erase(s);
        }
    }

    return 0;
}
