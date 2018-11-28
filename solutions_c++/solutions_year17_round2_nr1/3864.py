#include<bits/stdc++.h>

double max(double a,double b)
{
    return (a>b)?a:b;
}
void sol()
{
    double Max = -100000001;
    double tmps, tmpv, s;
    int n;
    scanf("%lf %d",&s,&n);
    for(int i=0;i<n;i++)
    {
        scanf("%lf %lf",&tmps,&tmpv);
        double t = (s-tmps)/tmpv;
        Max = max(t,Max);
    }
    printf("%.6lf\n",s/Max);
    return;
}
int main()
{
    int q;
    scanf("%d",&q);
    for(int i =1;i<=q;i++)
    {
        printf("Case #%d: ",i);
        sol();
    }

    return 0;
}
