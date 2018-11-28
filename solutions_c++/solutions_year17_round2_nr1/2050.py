#include<bits/stdc++.h>
#define ll long long
using namespace std;
ll arr[100100],t,n,m;
int main()
{
    long long d,n,k,s;
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        double ans=0;
        cin>>d>>n;
        for(int i=0;i<n;i++)
        {
            cin>>k>>s;
            double temp=((d-k)/((double)(s*1.0000)));
            ans=max(ans,temp);
            //cout<<ans<<endl;
        }
        double ans1=(d/(double)ans);
        cout<<"Case #"<<j<<": ";
        printf("%.8lf\n",ans1);
    }
return 0;
}
