#include <stdio.h>

int main()
{
    int T;
    scanf("%d", &T);
    for( int t=1; t<=T; t++ )
    {
        int d, n;
        scanf("%d %d", &d, &n);
        double maxT = 0;
        for( int i=0; i<n; i++ )
        {
            int k, s;
            scanf("%d %d", &k, &s);
            double tm = (d - k) / (double)s;
            if ( tm > maxT ) maxT = tm;
        }
        printf("Case #%d: %.6lf\n", t, d / maxT);
    }
    return 0;
}
