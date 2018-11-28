#pragma warning(disable:4996)

#include <stdio.h>

double d;
int n;
double k[1000];
double s[1000];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int t, tt=0;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%lf%d", &d, &n);

        if (tt==15)
            tt=tt;

        double m = -1;
        for (int i=0; i<n; i++)
        {
            scanf("%lf%lf", &k[i], &s[i]);
            double spd = d / ((d - k[i]) / s[i]);

            if (m<0 || m>spd)
                m = spd;
        }

        printf("Case #%d: %lf\n", ++tt, m);
    }

    return 0;
}
