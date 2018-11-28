#include <bits/stdc++.h>
using namespace std;
double min1(long arrk[],int arrs[],long n,long k)
{
    double mini=(float)k/(k-arrk[0])*arrs[0];
    for(int j=1;j<n;j++)
    {
        if((double)k/(k-arrk[j])*arrs[j]<mini)
           mini=(double)k/(k-arrk[j])*arrs[j];
    }

    return mini;
}
int main()
{
    std::ios::sync_with_stdio(false);
    freopen("a1.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,s[1000];
    long k,d,ki[1000];
    double ans;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>k>>d;
        for(int j=0;j<d;j++)
            cin>>ki[j]>>s[j];
        ans=min1(ki,s,d,k);
        cout<<"Case #"<<i<<": "<<std::fixed<<setprecision(8)<<ans<<endl;
    }
    return 0;
}
