#include <cstdio>

unsigned long long make_nondesc(unsigned long long val)
{
    unsigned long long result = val % 10;
    int lastd = val % 10; val /= 10;
    unsigned long long pow = 10;
    
    while (val)
    {
        if (val % 10 > lastd)
        {
            if (val % 10 == 0)
            {
                result = 0;
            }
            else
            {
                lastd = ((val % 10) - 1);
                result = pow - 1 + pow * lastd;
            }
        }
        else
        {
            lastd = val % 10;
            result += lastd * pow;
        }

        pow *= 10;
        val /= 10;
    }

    return result;
}

int main()
{
    freopen("tidy.in", "r", stdin);
    freopen("tidy.out", "w", stdout);

    int n;scanf("%d", &n);

    for (int i = 1; i <= n; ++i)
    {
        unsigned long long val;
        scanf("%lld", &val);
        printf("Case #%d: %lld\n", i, make_nondesc(val));
    }
    
    return 0;
}
