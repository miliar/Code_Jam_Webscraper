#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
bool f(ll n)
{
    ll next_digit = n%10;
    n = n/10;
    while (n)
    {
        ll digit = n%10;
        if (digit > next_digit)
            return false;
        next_digit = digit;
        n = n/10;
    }

    return true;
}
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
        ll j=1,t;
        cin>>t;
        while(j<=t)
        {
            ll n,i,p,q,r;
            cin>>n;
            for(i=n;i>=1;i--)
            {
                if(f(i))
                    break;
            }
            cout<<"Case #"<<j<<": "<<i<<endl;
            j++;
        }
}
