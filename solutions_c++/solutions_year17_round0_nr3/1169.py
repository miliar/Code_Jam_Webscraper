#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        ll i,n,m,mi,ma,p=1,num=0,ans=0;
        cin>>n>>m;
        while(num+p<m)
        {
            num+=p;
            p*=2;
        }
        if((n-num)%p>=m-num)
            ans=(n-num)/p+1;
        else ans=(n-num)/p;
        if(ans%2==0)
        {
            mi=ans/2-1;
            ma=ans/2;
        }
        else
        {
            mi=ans/2;
            ma=ans/2;
        }
        cout<<"Case #"<<tt<<": "<<ma<<" "<<mi<<"\n";
    }
    return 0;
}
