#include "bits/stdc++.h"
using namespace std;
typedef long long ll;
string s;
int main()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0.out","w",stdout);
    int t,tt=0;
    cin>>t;
    while(tt<t)
    {
        ll n,k;
        cin>>n>>k;
        //cout<<n<<' '<<k<<endl;
        n-=k;
        printf("Case #%d: ",++tt);
        ll i=0;
        while((1<<i)<=k)i++;
        i=1<<i;
        cout<<n/i+n%i/(i>>1)<<' '<<n/i;
        printf("\n");
    }
    return 0;
}
