#include <stdio.h>
#include <algorithm>
#include <cstring>
using namespace std;

int T;
int ind;
long long n,K, sol, cnt;
long long nr[2], val[2], aux_nr[2], aux_val[2];

void add(long long x, int i)
{
     for(int j=0;j<=1;j++)
        if( aux_val[j] == -1 || aux_val[j] == x )
        {
            aux_val[j] = x;
            aux_nr[j] += nr[i];
            break;
        }
}

void det()
{
    while(sol < K)
    {
        for(int i=0;i<=1;i++)
            aux_val[i] = -1, aux_nr[i] = 0;

        for(int i=0;i<=ind;i++)
        {
            long long x = val[i];
            if( x%2 == 0 )
            {
                 if( x/2 -1 > 0 ) add(x/2 - 1, i);
                 if( x/2 > 0 ) add(x/2, i);
            }
            else
            {
                if( x/2 > 0 ) add(x/2, i);
                if( x/2 > 0 ) add(x/2, i);
            }
        }

        ind = -1;
        for(int i=0;i<=1;i++)
           if( aux_val[i]!= -1)
               val[i]= aux_val[i], nr[i]= aux_nr[i], ind = i;

        sol += cnt;
        cnt *= 2;
    }

    long long res1, res2;
    int pos = 0;
    if( val[ind] > val[pos] ) pos = ind;

    cnt/=2; sol-=cnt;
    if( nr[pos] >= K-sol )
    {
        res1 = val[pos]/2;
        res2 = val[pos]/2; if( val[pos] %2 == 0) res2--;
    }
    else
    {
        res1 = val[!pos]/2;
        res2 = val[!pos]/2;  if( val[!pos] %2 == 0) res2--;
    }

    printf("%lld %lld\n",res1, res2);
}

int main()
{
    freopen("date.in","r",stdin);
    freopen("date.out","w",stdout);

    scanf("%d\n",&T);
    for(int it = 1; it<=T; it++)
    {
        printf("Case #%d: ",it);

        scanf("%lld %lld",&n, &K);

        if( K == n)
        {
            printf("0 0\n");
            continue;
        }

        ind = 0;
        nr[0] = 1; val[0] = n; nr[1] = 0; val[1] = -1;

        sol = 1; cnt = 2;
        det();
    }
    return 0;
}
