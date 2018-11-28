#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A.in","r",stdin);
    freopen("A3.out","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        double d;
        int n;
        double an=10000000.0;
        cin>>d>>n;
        for(int i=1;i<=n;i++)
        {
            double k,s;
            cin>>k>>s;
            if(i==1)
                an=(d-k)/s;
            else
                an=max(an,(d-k)/s);
        }
        printf("Case #%d: %.7f\n",i,d/an);
    }
}
