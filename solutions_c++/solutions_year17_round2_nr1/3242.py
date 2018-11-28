#include <iostream>
#include <limits.h>
using namespace std;

int main()
{
    long t=0,n=0,d=0,s=0,k=0;
    
    cin>> t;
    
    for(int u=1;u<=t;u++)
    {
        cin>>d>>n;
        double ans=-1.0;
        
        for(int i=1;i<=n;i++)
        {
            cin>>k>>s;
            double temp=(d-k)/(double)(s);
            ans=max(ans,temp);
        }
        cout<<"Case #"<<u<<": "<<fixed<<d/(double)ans<<"\n";
    }
    return 0;
}

