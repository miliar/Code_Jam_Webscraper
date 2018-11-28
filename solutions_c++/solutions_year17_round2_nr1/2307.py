#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long long n,d,tc;
    cin>>tc;
    for(int t=1;t<=tc;t++)
    {
        double maxtime=-1;
        cin>>d>>n;
        long long k,s;
        for(int i=0;i<n;i++)
        {
            cin>>k>>s;
            maxtime=max(maxtime*1.l,1.l*(d-k)/s);
        }
        cout<<fixed<<setprecision(10)<<"Case #"<<t<<": "<<d/maxtime<<endl;
    }
}