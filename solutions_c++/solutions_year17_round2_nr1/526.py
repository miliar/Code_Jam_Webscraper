#include<stdio.h>

int n;
double d;
double k[1000]={0}, s[1000]={0};
double time[1000]={0};

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out","w",stdout);
    int test, t, i;
    scanf("%d",&test);
    for(t=1;t<=test;t++){
        double ans = -1.0;
        scanf("%lf%d",&d,&n);
        for(i=0;i<n;i++) scanf("%lf%lf",&k[i], &s[i]);
        for(i=0;i<n;i++){
            time[i] = (d - k[i]) / s[i];
            if(ans < time[i]) ans = time[i];
        }
        printf("Case #%d: %.8lf\n", t, d / ans);
    }
    return 0;
}
