#include <stdio.h>
#include <string.h>

typedef long long LL;

int c[2][2];
LL a[2][2];
LL res_l, res_r;

void cal(LL n, LL k)
{
    c[0][0] = 1;
    a[0][0] = n;
    c[0][1] = 0;
    a[0][1] = n;
    for(int i=0;;i++)
    {
        int p = i%2;
        int q = (i+1)%2;
        c[q][0] = 0;
        c[q][1] = 0;
        for(int j=0;j<2;j++)
        {
            if( a[p][j] % 2 )
            {
                res_l = a[p][j] / 2;
                res_r = a[p][j] / 2;
                if( k <= c[p][j] )
                {
                    return;
                }
                a[q][j] = res_l;
                c[q][j] += c[p][j]*2;
            }
            else
            {
                res_l = a[p][j] / 2;
                res_r = (a[p][j] - 1) / 2;
                if( k <= c[p][j] )
                {
                    return;
                }
                a[q][0] = res_l;
                a[q][1] = res_r;
                c[q][0] += c[p][j];
                c[q][1] += c[p][j];
            }
            k-= c[p][j];
        }
    }
}

int main()
{
    int T;
    scanf("%d", &T);
    for(int ca=1;ca<=T;ca++)
    {
        LL n,k;
        scanf("%lld%lld", &n, &k);
        cal(n, k);
        printf("Case #%d: %lld %lld\n", ca, res_l, res_r);
    }
    return 0;
}

