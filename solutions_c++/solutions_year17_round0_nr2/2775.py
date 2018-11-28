#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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

void printa(int* a, int &al) {
    for(int i = al - 1; i >= 0; i--)
        printf("%d", a[i]);
    printf("\n");
}

unsigned long long unsignedLongLongRand()
{
    unsigned long long rand1 = abs(rand());
    unsigned long long rand2 = abs(rand());
    rand1 = rand1 << (sizeof(int)*8);
    unsigned long long randULL = (rand1 | rand2);
    return randULL;
}

long long gentest() {
    long long lld = unsignedLongLongRand();
    printf("%lld\n", lld);
    return lld;
}

int solving(int t)
{
    long long g;
    scanf("%lld", &g);

    //g = gentest();

    int a[100], al;

    if (g < 10)
    {
        printf("Case #%d: %lld\n", t, g);
    }
    else
    {
        longToArray(g, a, al);
        a[al] = 0;

        for (int i = 0; i < al; i++) {
            if (a[i] < a[i+1]) {
                a[i+1]--;
                for (int j = 0; j <= i; j++)
                    a[j] = 9;
            }
        }

        //printa(a, al);

        long long result = 0;

        for (int i = al-1; i >= 0; i--) {
            result *= 10;
            result += a[i];
        }





        printf("Case #%d: %lld\n", t, result);
    }
}

int main()
{
    int t, T;
    scanf("%d", &T);

    for (int t = 1; t <= T; t++)
        solving(t);

    return 0;
}
