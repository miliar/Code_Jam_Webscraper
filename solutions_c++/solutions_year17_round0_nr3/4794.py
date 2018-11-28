#include "bits/stdc++.h"
using namespace std;
typedef unsigned long long ull;
typedef long long int ll;
typedef vector<long long int> vi;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("output.out","w",stdout);
    ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);
    ll t;
    cin>>t;
    int z=1;
    while(t--)
    {
        ll n,sum=0,count=0,m,flag=0,ans=0,k,a1,a2;
        cin>>n>>m;
        map<ll,ll> ma;
        ma[n]++;
        k=n;
        while(n>0&&n>k-m)
        {
            //cout<<n<<endl;
            map<ll,ll>::iterator it=ma.end();
            it--;
            if((it->first)%2==1)
                a1=a2=((it->first)/2),ma[(it->first)/2]+=(it->second)*2,n-=(it->second),ma.erase(it);
            else
                a1=((it->first)/2),a2=((it->first)/2)-1,ma[(it->first)/2]+=(it->second),ma[((it->first)/2)-1]+=(it->second),n-=(it->second),ma.erase(it);
        }
        cout<<"Case #"<<z<<": "<<a1<<" "<<a2<<endl;
        z++;
    }
    return 0;
}


/* freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
 */
