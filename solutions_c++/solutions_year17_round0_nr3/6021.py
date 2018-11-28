#include "bits/stdc++.h"
using namespace std;
typedef unsigned long long ull;
typedef long long int ll;
typedef vector<long long int> vi;
int main()
{
    freopen("C-small-2-attempt1.in","r",stdin);
    freopen("output.out","w",stdout);
    ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);
    ll n,sum=0,count=0,m,flag=0,ans=0,k,t;
    cin>>t;
    int z=1;
    while(t--)
    {
        ll a1,a2;
        multiset<ll> s;
        cin>>n>>m;
        s.insert(n);
        s.insert(0);
        while(m--)
        {
            auto it=s.end();
            it--;
            ll n=*it;
            //cout<<n<<endl;
            if(n%2!=1)
                a1=(n/2),a2=max((ll)0,(n/2)-1);
            else a1=(n/2),a2=(n/2);
            if(n!=0)
            {
                s.erase(s.find(n));
                if(n%2==0)
                    s.insert(n/2),s.insert((n/2)-1);
                else s.insert(n/2),s.insert(n/2);
            }
            else break;
        }
        cout<<"Case #"<<z<<": "<<a1<<" "<<a2<<endl;
        z++;
    }
    return 0;
}


/* freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
 */
