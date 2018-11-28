#include<bits/stdc++.h>
using namespace std;


int main()
{
    freopen("A-large23.in", "r", stdin);
    freopen("output.in", "w", stdout);
    int t,i,j;
    scanf("%d",&t);
    for(int ca=1; ca<=t; ca++)
    {
        double d,t,sp,cp;
        int n;
        scanf("%lf %d",&d,&n);
        t=0.0;
        for(i=1; i<=n; i++)
        {
            scanf("%lf %lf",&cp,&sp);
            t=max(t,(d-cp)/sp);
        }
        printf("Case #%d: %.12lf\n",ca,d/t);
    }
}

