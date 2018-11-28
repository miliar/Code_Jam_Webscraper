#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;

int main()
{
    int T;
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    cin>>T;
    for(int i=1;i<=T;i++)
    {
        long double D,N;
        cin>>D>>N;
        long double d,s;
        cin>>d>>s;
        long double mx = (D-d)/s;
        for(int j=2;j<=N;j++)
        {
            cin>>d>>s;
            long double tmp = (D-d)/s;
            mx=max(mx,tmp);
        }
        cout<<"Case #"<<i<<": ";
        printf("%.6Lf\n",D/mx);
    }
    return 0;
}
