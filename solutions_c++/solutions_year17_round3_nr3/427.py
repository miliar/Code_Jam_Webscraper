#include<bits/stdc++.h>
using namespace std;

double er=1e-9,pr[100];

int main()
{
   freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
   int t,ts;
   scanf("%d",&ts);
   for(int t=1;t<=ts;t++)
   {
       int n,k; double ans=0,u;
       scanf("%d%d",&n,&k);
       scanf("%lf",&u);
       for(int i=0;i<n;i++)
         scanf("%lf",&pr[i]);


       double a=0,b=1.00,mid,tot,mul;
       for(int i=0;i<1000;i++)
       {
           mid=(a+b)/2.00;
           tot=0;mul=1;
           for(int i=0;i<n;i++)
           {
               if(pr[i]<mid)
               {
                   tot+=mid-pr[i];mul*=(mid);
               }
               else mul*=pr[i];
           }

           if(tot>u) b=mid;
           else
           {
               ans=max(ans,mul);a=mid;
           }
       }

       printf("Case #%d: %0.10lf\n",t,ans);


   }


}
