#include <cstdio>

void caser(int casen)
{
    int n, k;
    scanf("%d %d", &n, &k);

    int x = k >> 1, l = 0;
    while(x != 0)
    {
        l++;
        x >>= 1;
    }

    k -= (1 << l);
    n -= (1 << l) - 1;

    int base = n / (1 << l);
    int countHigher = n % (1 << l);

    if(k < countHigher)
        base++;

     printf("Case #%d: %d %d\n", casen, base / 2, base & 1 ? base / 2 : base / 2 - 1);
}

int main()
{
    int n;
    scanf("%d", &n);
    for(int i = 1; i <= n; i++)
        caser(i);
    return 0;
}