#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const long long N = 1005;
long long D, k[N], v[N];
int n;

int main()
{
    int T;
    scanf("%d", &T);
    for(int Case = 1; Case <= T; ++Case)
    {
        double vans;
        scanf("%lld%d", &D, &n);
        for(int i = 1; i <= n; ++i)
        {
            scanf("%lld%lld", &k[i], &v[i]);
            if(i == 1) vans = (double)v[i] + (double)k[i]*(double)v[i]/(double)(D-k[i]);
            else
            {
                double vv = (double)v[i] + (double)k[i]*(double)v[i]/(double)(D-k[i]);
                if(vv < vans) vans = vv;
            }
        }
        
        
        printf("Case #%d: %.6lf\n", Case, vans);
    }

    return 0;
}
