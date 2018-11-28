#include <bits/stdc++.h>
using namespace std;

int main()
{    int t,count=0;
    cin>>t;
     while(t--)
    {   count++;
        long long int n;
        long double d,k,v;
        cin>>d>>n;
        long double a[n],speed;
        for(int i=0;i<n;i++)
        {
            cin>>k>>v;
            a[i]=(d-k)/v;
        }
        sort(a,a+n);
        speed=(d/a[n-1]);
        //printf("Case # %d: %lf\n",count,speed);
        cout<<"Case #"<<count<<": ";
        cout<<setprecision(6)<<fixed<<speed<<endl;
    }
    return 0;
}
