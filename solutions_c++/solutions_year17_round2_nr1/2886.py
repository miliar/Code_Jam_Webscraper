#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,e;
   // ofstream outFile;

//outFile.open("outputfr.txt");
    scanf("%d",&t);
    for(e=1;e<=t;e++)
    {
        int d,n;
        scanf("%d%d",&d,&n);
        int i;
        int k[n+2];
        int s[n+2];
        for(i=1;i<=n;i++)
        {
            scanf("%d%d",&k[i],&s[i]);
        }

        long double ans,r,m=(long double)-1;
        for(i=1;i<=n;i++)
        {
            r=(long double)(d-k[i])/s[i];
            if(r>m)
                m=r;
        }
        ans=(long double)d/m;
       // outFile.precision(9);
       // outFile.setf(ios::fixed);
       //outFile.setf(ios::showpoint);
       // outFile<<"Case #"<<e<<": "<<ans<<"\n";
        printf("Case #%d: %.9f\n",e,(double)ans);

    }
}
