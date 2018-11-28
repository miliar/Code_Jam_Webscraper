#include<bits/stdc++.h>
using namespace std;

int main()
{
    FILE *f, *g;
    f = fopen("in.txt","r");
    g = fopen("out.txt","w");
    long long int t,tx,d,n,k,s,i;
    fscanf(f,"%lld",&t);
    tx = t;
    while(t--)
    {
        fscanf(f,"%lld %lld",&d,&n);
        double tt = 0;
        for(i=0;i<n;i++)
        {
            fscanf(f,"%lld %lld",&k,&s);
            double t1 = (d-k)/(s*1.0);
            if(t1 > tt)
            {
                tt = t1;
            }
        }
        double ans = d/(tt);
        fprintf(g,"Case #%lld: %0.8lf\n",tx-t,ans);
    }
    return(0);
}
