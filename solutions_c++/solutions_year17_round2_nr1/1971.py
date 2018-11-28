#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for (int ii=0; ii<t; ii++)
    {
        int dis, n;
        cin>>dis>>n;
        double mx=0;
        for (int i=0; i<n; i++)
        {
            int p,s;
            cin>>p>>s;
            double k=(0.0+dis-p)/s;
            mx=max(mx,k);
        }
        cout<<"Case #"<<ii+1<<": "<<setprecision(15)<<fixed<<dis/mx<<endl;
    }
}
