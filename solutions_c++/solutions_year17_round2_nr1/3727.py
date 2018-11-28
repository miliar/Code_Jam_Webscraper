#include<bits/stdc++.h>

using namespace std;
#define lol long long
int main()
{
    lol int i,j,k,n,t,d,s,tcase=0;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    cin>>t;
    while(t--)
    {
        tcase++;
        double mx=-1.0;
        cin>>d>>n;
        while(n--)
        {
            scanf("%lld %lld",&k,&s);
            double ff=(double)(d-k);
            double yy=(double)s;
            double hh=ff/yy;
            double zz=(double)(hh);
            if(zz>mx)mx=zz;
        }
        double a=(double)d;
        double b=(double)mx;
        double res=a/b;
        printf("Case #%lld: %lf\n",tcase,res);
    }



    return 0;
}
