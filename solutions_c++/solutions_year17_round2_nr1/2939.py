#include<bits/stdc++.h>
using namespace std;

double hr[2000][2],init,eps=0.000000001;
int n;

bool ok(double sp)
{
    bool f=1;
    for(int i=0;i<n;i++)
    {
        double t1=init/sp,t2=(init-hr[i][0])/hr[i][1];
        if(fabs(t1-t2)<=eps) continue;
        if(t1<t2) return 0;
    }
    return 1;
}

int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
    int t,ts;
    scanf("%d",&ts);
    for(t=1;t<=ts;t++)
    {
        double mn=0;
        scanf("%lf%d",&init,&n);
        for(int i=0;i<n;i++)
        {
            double sp,pos;
            scanf("%lf%lf",&pos,&sp);
            mn=max(mn,(init-pos)/sp);
        }
        double ans=init/mn;
        printf("Case #%d: %0.6lf\n",t,ans);



    }



}
