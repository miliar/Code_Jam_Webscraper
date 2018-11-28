#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
    freopen("A-large(1).in","r",stdin);
    freopen("A-large(1).out","w",stdout);
    ll t;
    cin>>t;
    for(ll tt=1;tt<=t;tt++)
    {
        string s;
        ll k;
        cin>>s>>k;
        ll flip=0,n=s.length();
        for(ll i=0;i<n-k+1;i++)
        {
            if(s[i]=='-')
            {
                flip++;
                for(ll j=i;j<=i+k-1;j++)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
            }
        }
        bool ha=true;
        for(ll i=0;i<n;i++)
        {
            if(s[i]=='-')
            {
                ha=false;
                break;
            }
        }
        printf("Case #%lld: ",tt);
        if(ha)
            cout<<flip<<endl;
        else
            cout<<"IMPOSSIBLE\n";
    }
    return 0;
}