#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t,tt=1;
    cin>>t;
    while(tt<=t)
    {
        long long d,k;
        int s,n;
        cin>>d>>n;
        double mn=-1;
        for(int i=0; i<n; i++)
        {
            cin>>k>>s;
            mn=max(mn,double(d-k)/s);
        }
        printf("Case #%d: %.06f\n",tt,d/mn);
        tt++;
    }
    return 0;
}
