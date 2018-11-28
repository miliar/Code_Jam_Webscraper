#include <stdio.h>
#include <string.h>

int main()
{
    int T;
    scanf("%d", &T);
    for(int ca=1;ca<=T;ca++)
    {
        int n;
        double D;
        scanf("%lf%d", &D, &n);
        double p = 0;
        for(int i=0;i<n;i++)
        {
            double ki, si;
            scanf("%lf%lf", &ki, &si);
            double pi = D * si / (D - ki);
            if( 0 == i || pi < p )
            {
                p = pi;
            }
        }
        printf("Case #%d: %f\n", ca, p);
    }

    return 0;
}

