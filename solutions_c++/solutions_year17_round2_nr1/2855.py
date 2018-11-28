#include <stdio.h>

int T,D,N,K,S;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("AoutputL.out","w",stdout);

    scanf("%d", &T);
    for (int i = 1; i <= T; i++)
    {
        double max = 0;
        scanf("%d%d", &D,&N);
        for (int j = 0; j < N; j++)
        {
            scanf("%d%d", &K, &S);
            double temp = ((double)D-K)/S;
            if(max < temp)
            {
                max = temp;
            }
        }
        printf("Case #%d: %.6lf\n", i, D/max);
    }
    return 0;
}