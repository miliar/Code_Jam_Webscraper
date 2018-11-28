#include <bits/stdc++.h>
#define ll long long int
#define fs first
#define sc second
#define pb push_back
#define ppb pop_back
#define pii pair<int,int>
#define pil pair<int,ll>
#define vll vector<ll>
#define vi vector<int>
#define d0(x) cout<<x<<" "
#define d1(x) cout<<x<<"\n"
#define d2(x,y) cout<<x<<" "<<y<<"\n"
#define d3(x,y,z) cout<<x<<" "<<y<<" "<<z<<"\n"
const ll mod=1e9+7;ll ans1,ans2;
using namespace std;
void build(ll n,ll k)
{
    if(k==1&&n<1){ans1=0;ans2=0;return;}
   if(k==1){n--;ans1=n/2;ans2=(n/2)+(n%2);return;}
   n--;k--;ll n1=n/2;ll n2=n1+(n%2),k1=k/2;ll k2=k1+(k%2);
   if(n2>n1&&k2>k1){build(n2,k2);return;}
       build(n1,k2);

}
int main()
{
    ios_base::sync_with_stdio ( false );
    ofstream outp("output.txt");
    ifstream inp("input.txt");
    int t;inp>>t;
    for(int test=1;test<=t;test++)
    {
        ll n,k1;inp>>n>>k1;
        build(n,k1);
        outp<<"Case #"<<test<<": "<<ans2<<" "<<ans1<<"\n";

    }
}
