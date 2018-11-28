#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int x=1;
    while(x<=t)
    {
        long long d;
        int n;
        cin>>d>>n;
        int darr[n];
        int sarr[n];
        int i=0;
        for(i=0;i<n;i++)
        {
            cin>>darr[i]>>sarr[i];
        }
        double tm=0;
        for(i=0;i<n;i++)
        {
            double x,y;
            x=(double)(d-darr[i])/sarr[i];
            if(i==0)
                tm=x;
            else
                tm=max(x,tm);
        }
        double ans=(double)d/tm;
        cout<<"Case #"<<x<<": ";
        printf("%lf\n",ans);
        x++;
    }
  return 0;
}
