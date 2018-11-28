#include <bits/stdc++.h>
#define ll long long
#define wh(t) while(t--)
using namespace std;

bool areSorted(ll int n)
{
    ll int next_digit = n%10;
    n = n/10;
    while (n)
    {
        ll int digit = n%10;
        if (digit > next_digit)
            return false;
        next_digit = digit;
        n = n/10;
    }

    return true;
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    ll int t,i,j,n,m;
    cin>>t;
    for(int k=0;k<t;k++)
    {
        cin>>n;
        for(i=n; i>0; i--)
        {
            if(areSorted(i))
            {
                j=i;
                break;
            }
        }
        cout<<"Case #"<<k+1<<": "<<j<<endl;
    }
    return 0;
}

