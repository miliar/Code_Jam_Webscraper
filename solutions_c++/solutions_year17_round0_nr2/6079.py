#include <stdio.h>
#include <string.h>

const int MX = 1010;
int res[MX];

bool non_des(int n)
{
    int pre_k = 9;
    while(n)
    {
        int k = n%10;
        n /= 10;
        if( k > pre_k ) return false;
        pre_k = k;
    }
}

void pre_init()
{
    int pre_n = 0;
    for(int i=0;i<MX;i++)
    {
        if( non_des(i) )
        {
            pre_n = i;
            res[i] = i;
        }
        else
        {
            res[i] = pre_n;
        }
    }
}

int main()
{
    int T;
    scanf("%d", &T);
    pre_init();
    for(int ca=1;ca<=T;ca++)
    {
        int n;
        scanf("%d", &n);
        printf("Case #%d: %d\n", ca, res[n]);
    }
    return 0;
}

