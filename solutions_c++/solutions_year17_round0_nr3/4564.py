#include<bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef long double ld;
typedef set<int>::iterator sit;
typedef map<int,int>::iterator mit;
typedef vector<int>::iterator vit;

int main()
{
   ll t;
   cin>>t;
   multiset<ll> m;
    for(int u=1;u<=t;u++)
   {
       ll n,k;
       cin>>n>>k;
       m.insert(n);
       for(ll i=1;i<k;i++)
       {
           ll x=*(m.rbegin());
           m.erase(--m.end());
           if(x%2==0)
           {
               m.insert((x-1)/2);
               m.insert(x/2);
           }
           else
            {
                m.insert(x/2);
                m.insert(x/2);
            }
       }
       ll x=*(m.rbegin());
       if(x%2==0)
        cout<<"Case #"<<u<<": "<<x/2<<" "<<(x-1)/2<<endl;
        else
        cout<<"Case #"<<u<<": "<<x/2<<" "<<x/2<<endl;
    m.clear();
   }
    return 0;
}
