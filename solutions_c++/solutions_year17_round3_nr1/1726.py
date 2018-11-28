#include <stdio.h>
#include <algorithm>
#include <math.h>
struct pancake
{
    long long r,h;
    double areaLateral;
};
pancake p[1001];
int t,n,k;
double pi = acos(-1);
double aSum, rMax, aMin;
double salida;
bool pancakesorter(pancake const& a, pancake const& b)
{
    if(a.areaLateral == b.areaLateral)
        return a.r > b.r;
    return a.areaLateral > b.areaLateral;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("large.txt","w",stdout);
    scanf("%d",&t);
    for(int x = 0; x < t; x++)
    {
        scanf("%d %d",&n,&k);
        for(int y = 0; y < n; y++)
        {
            scanf("%lld %lld",&p[y].r,&p[y].h);
            p[y].areaLateral = 2 * pi * p[y].r * p[y].h;
        }
        std::sort(p, p + n, pancakesorter);
        aSum = 0;
        rMax = 0;
        aMin = -1;
        for(int y = 0; y < k; y++)
        {
            aSum += p[y].areaLateral;
            if(p[y].r > rMax)
                rMax = p[y].r;
            if(aMin == -1 || p[y].areaLateral < aMin)
                aMin = p[y].areaLateral;
        }
        salida = aSum + (pi * rMax * rMax);
        for(int y = k; y < n; y++)
        {
            if(p[y].r > rMax)
            {
                double tSalida = aSum - aMin + p[y].areaLateral + (pi * p[y].r * p[y].r);
                if(tSalida > salida)
                    salida = tSalida;
            }
        }
        printf("Case #%d: %.8f\n", x + 1, salida);
    }
    return 0;
}


