#include <cstdio>
long long v[101], c[101][2];
main()
{
    freopen("C-large (1).in","r",stdin);
    freopen("C_L.txt","w",stdout);
    long long t, k, x; scanf("%lld",&t);
    bool w;
    for(long long it = 1;it <= t;it++)
    {
        scanf("%lld %lld",&v[0],&k);
        c[0][0] = 1; c[0][1] = 0;
        for(int i = 0;i < 66;i++)
        {
            v[i+1] = v[i]/2;
            if(v[i]%2 == 0)
            {
                c[i+1][0] = c[i][0];
                c[i+1][1] = c[i][0] + c[i][1]*2;
            }
            else
            {
                c[i+1][0] = c[i][1] + c[i][0]*2;
                c[i+1][1] = c[i][1];
            }
        }
        x = 0; w = true;
        for(int i = 0;w && i < 66;i++)
        for(int j = 0;w && j < 2;j++)
        {
            x += c[i][j];
            if(x >= k)
            {
                printf("Case #%lld: %lld %lld\n",it,(v[i]-j)/2,(v[i]-j-1)/2);
                w = false;
            }
        }
    }
}
