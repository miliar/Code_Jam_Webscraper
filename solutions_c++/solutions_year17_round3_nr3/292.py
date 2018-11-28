#include<stdio.h>
int n, k;
double U, ans;
double arr[51];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i, tt, T;
    scanf("%d", &T);
    double l, r;
    for(tt=1; tt<=T; ++tt)
    {
        ans = 1;
        scanf("%d%d", &n, &k);
        scanf("%lf", &U);
        l=r=1.000000;
        for(i=1; i<=n; ++i)
        {
            scanf("%lf", &arr[i]);
            ans *= arr[i];
            if(l>arr[i]) l=arr[i];
        }
        for(int c=1; c<=1000; ++c)
        {
            double m = (l+r)/2, tmp=1, cost=0;
            for(i=1; i<=n; ++i)
            {
                if(m <= arr[i]) tmp*=arr[i];
                else { tmp*=m; cost += m-arr[i]; }
            }
            if(cost>U)
            {
                r = m;
            }
            else
            {
                ans = ans<tmp?tmp:ans;
                l = m;
            }
        }
        printf("Case #%d: %.6f\n", tt, ans);
    }
}
