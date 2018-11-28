#include<stdio.h>
#include<stdlib.h>
#include<cstring>
char c[19];
long long t;
int l;
char sol[19];
bool bt(int pos, int y)
{
    if(pos == l)
        return true;
    int d = c[pos] - '0';
    if(d < y)
        return false;
    bool r;
    r = bt(pos + 1, d);
    if(r)
    {
        sol[pos] = c[pos];
    }
    else
    {
        if(c[pos] - 1 - '0' < y)
            return false;
        sol[pos] = c[pos] - 1;
        for(int z = pos + 1; z < l; z++ )
            sol[z] = '9';
    }
    return true;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%lld",&t);
    for(int x = 0; x < t; x++)
    {
        scanf("%s",c);
        l = strlen(c);
        sol[l] = c[l];
        bt(0,0);
        long long salida = 0;
        for(int y = 0; y < l; y++)
        {
            salida *= 10;
            salida += sol[y] - '0';
        }
        printf("Case #%d: %lld\n", x+1,salida);
    }
}

