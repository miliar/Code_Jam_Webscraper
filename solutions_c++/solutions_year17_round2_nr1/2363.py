#include <bits/stdc++.h>

using namespace std ;

int main()
{
    freopen("A-large.in" , "r" , stdin);
    freopen("outputA.txt" , "w" , stdout);

    int test_case ;

    scanf("%d", &test_case);

    for(int i = 0 ; i < test_case ; i++)
    {
        int K;
        double D ,pos , speed ;
        double max_time = 0.0;
        scanf("%lf %d", &D , &K);

        for(int j = 0 ; j < K ; j++)
        {
            scanf("%lf %lf", &pos , &speed);

            double time = 1.0*(1.0*D - pos) / (1.0*speed);
            max_time = max(max_time , time);
        }
        double ans = D / max_time;

        printf("Case #%d: %.10f\n",i+1 , ans);
    }



}
