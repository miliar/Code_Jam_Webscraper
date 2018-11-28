#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
double su;
double aa[55];
int n,k;
bool judge(double x)
{
    double xx=su;
    for(int i=0;i<n;i++)
    {
        if(x>aa[i])
            xx-=(x-aa[i]);
        if(xx<0) return false;
    }
    return true;
}
double ef(double l, double r)
{
    //cout<<"Q "<<l<<" "<<r<<endl;
    if(abs(l-r)<1e-13)
    {
        return l;
    }
    double mid=(l+r)/2;
    if(judge(mid))
    {
        return ef(mid,r);
    }
    else return ef(l,mid);
}
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=0;cas<t;cas++)
    {
        scanf("%d%d",&n,&k);
        scanf("%lf",&su);
        for(int i=0;i<n;i++)
            scanf("%lf",&aa[i]);
        double p=ef(0.0,1.0);
        //cout<<"P "<<p<<endl;
        double pos=1.0;
        for(int i=0;i<n;i++)
        {
            if(aa[i]>p)
            pos*=(aa[i]);
            else pos*=(p);
        }
        printf("Case #%d: %f\n",cas+1,pos);
    }

}
