#include <bits/stdc++.h>
#define ll long long int
#define mod 1000000007
using namespace std;

ll t,tt,d,n,i,a,b;
double ans;
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);

    cin>>t;
    tt=t;
    while(t)
    {
        cin>>d>>n;
        ans=0.0;
        for(i=0;i<n;i++)
        {
            cin>>a>>b;
            double k = ((d-a)*1.0)/b;
            ans=max(ans,k);
        }
        double k = (d*1.0)/ans;
        cout<<"Case #"<<tt-t+1<<": ";
        printf("%0.12f\n",k);
        t--;
    }

    return 0;
}
