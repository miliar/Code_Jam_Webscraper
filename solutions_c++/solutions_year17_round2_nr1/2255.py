#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.in", "r" , stdin);
    freopen("output.out", "w", stdout);
    int caseno=0,t;
    cin>>t;
    long long int ci=1;
    while(caseno++<t)
    {
        double n,d,k[1005]={0},s[1005]={0};
        cin>>d>>n;
        for(int i=0;i<n;i++)
        {
            cin>>k[i]>>s[i];
        }
        double time=0;
        for(int i=n-1;i>=0;i--)
        {
            time=max(time,(d-k[i])/s[i]);
        }
        cout<<"Case #"<<caseno<<": ";
        cout<<setprecision(10)<<d/time<<"\n";
    }
    return 0;
}
