#include "bits/stdc++.h"
using namespace std;
typedef unsigned long long ull;
typedef long long int ll;
typedef vector<long long int> vi;
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.out","w",stdout);
    ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);
    ll t;
    cin>>t;
    int z=1;
    while(t--)
    {
        ll n,sum=0,count=0,m,flag=0,ans=0,k,t;
        cin>>n;
        while(n)
        {
            m=n;
            flag=0;
            int x=10;
            while(m)
            {
                int y=m%10;
                if(y>x)
                    break;
                m=m/10;
                x=y;
            }
            if(m==0)
            {
                ans=n;
                break;
            }
            n--;
        }
        cout<<endl;
        cout<<"Case #"<<z<<": ";
        cout<<ans;
        cout<<endl;
        z++;
    }
    return 0;
}


/* freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
 */
