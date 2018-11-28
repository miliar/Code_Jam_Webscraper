#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t,j;
    cin>>t;
    for(j=1;j<=t;j++)
    {
       int n,d;
       cin>>d>>n;
  //     int arr[n];
       double max=0;
       double ans;
       for(int i=0;i<n;i++)
       {
           int k,s;
           cin>>k>>s;
           ans=(double)(d-k)/s;
           if(ans>max)
           {
               max=ans;
           }
       }
        double res;
        res=d/max;
        printf("Case #%d: %lf\n",j,res);
    }
return 0;
}
