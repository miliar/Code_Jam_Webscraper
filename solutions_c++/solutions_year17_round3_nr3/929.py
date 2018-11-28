#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);

    int t;
    cin>>t;

    for(int x=1;x<=t;x++)
    {
        int n,k;
        cin>>n>>k;
        double d;cin>>d;

        double a[n];

        for(int i=0; i<n; i++)
            cin>>a[i];

        double ats = 1.0;

        double l = 0.0;
        double r = 1.0;

        for(int z=0; z<200;z++)
        {
            double b[n];

            for(int i=0;i<n;i++)
                b[i]=a[i];

            double mid = l + (r-l)/2.0;
            double temp = d;

            for(int i=0; i<n; i++)
            {
                if(b[i] < mid)
                {
                    temp-=mid-b[i];
                    b[i]=mid;
                }
            }

            if(temp>=0.0)l=mid;
            else r=mid;
           // cout<<l<<"  "<<r<<" "<<temp<<"\n";
        }

        for(int i=0; i<n; i++)
            ats*=max(l,a[i]);


        cout<<"Case #"<<x<<": "<<fixed<<setprecision(30)<<ats<<"\n";

    }




return 0;
   }

