#include <cstdio>

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);

    for (int i = 1; i <= t; ++i)
    {
        int d, hcount;
        double spd;
        scanf("%d%d", &d, &hcount);

        double crtspd, x0;
        scanf("%lf%lf", &x0, &crtspd);
        double dt = (d - x0)/crtspd;
        
        for (int j = 1; j < hcount; ++j)
        {
            scanf("%lf%lf", &x0, &crtspd);
            if ((d-x0)/crtspd > dt)
            {
                dt = (d-x0)/crtspd;
            }
        }

        printf("Case #%d: %.6f\n", i, (d/dt));
    }
    
    return 0;
}
