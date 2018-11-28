#include<iostream>
#include<string>
#include<map>
#include<queue>
using namespace std;
int main()
{
    int t,tc,i;
    cin>>t;
    int k[1002],s[1002],d,n;
    for(tc=1;tc<=t;tc++)
    {
        cout<<"Case #"<<tc<<": ";
        cin>>d>>n;
        for(i=0;i<n;i++)
        {
            cin>>k[i]>>s[i];
        }
        double max_t=0,ans;
        for(i=0;i<n;i++)
        {
            max_t=max(max_t,1.0*(d-k[i])/s[i]);
        }
        ans=1.0*d/max_t;
        printf("%.6lf\n",ans);
    }
    return 0;
}