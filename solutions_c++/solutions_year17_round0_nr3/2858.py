#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <map>

#define lld long long
#define llu unsigned long long

using namespace std;

void longToArray(long long g, int* a, int &al)
{
    long long gg = g;
    al = 0;
    while (gg > 0)
    {
        a[al] = gg % 10;
        gg = gg / 10;
        al++;
    }
}

void printa(int* a, int &al)
{
    for(int i = al - 1; i >= 0; i--)
        printf("%d", a[i]);
    printf("\n");
}

unsigned long long unsignedLongLongRand()
{
    unsigned long long rand1 = abs(rand());
    unsigned long long rand2 = abs(rand());
    rand1 = rand1 << (sizeof(int) * 8);
    unsigned long long randULL = (rand1 | rand2);
    return randULL;
}

int solving(int t)
{
    lld g, k;
    scanf("%lld %lld", &g, &k);

    lld min = 0;
    lld max = 0;

    std::map<lld, lld> mp;

    mp[g] = 1LL;

    lld kk = k - 1;
    while(kk > 0)
    {

        lld second = mp.rbegin()->second;
        if (second <= kk)
        {
            lld first = mp.rbegin()->first;
            mp.erase(mp.find(first));

            lld mx = first / 2;
            lld mn = first - mx - 1;

            if (mx > 0)
                mp[mx] += second;
            if (mn > 0)
                mp[mn] += second;

            kk -= second;
        }
        else
        {
            break;
        }
    }

    if (mp.rbegin()->first > 1)
    {
        max = mp.rbegin()->first / 2;
        min = mp.rbegin()->first - max - 1;
    }
    else
    {
        max = 0;
        min = 0;
    }

    printf("Case #%d: %lld %lld\n", t, max, min);
    //fflush(stdout);
}

int main()
{
    int t, T;
    scanf("%d", &T);

    for (int t = 1; t <= T; t++)
        solving(t);

    return 0;
}
