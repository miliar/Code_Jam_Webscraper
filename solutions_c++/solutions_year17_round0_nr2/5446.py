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
const ll mod=1e9+7;int s[2000];
using namespace std;
bool fn(ll n)
{
    int dg=9;bool ans=true;
    while(n>0)
    {
        if(n%10>dg)
        {
            ans=false;
        }
        dg=n%10;n=n/10;
    }
    return ans;
}
int main()
{
    ios_base::sync_with_stdio ( false );
    ofstream outp("output.txt");
    ifstream inp("input.txt");
    int t;inp>>t;
    s[1]=1;
    for(int i=2;i<1001;i++)
    {
        if(fn(i))
        {
            s[i]=i;
        }
        else
        {
            s[i]=s[i-1];
        }
    }
    for(int test=1;test<=t;test++)
    {
        int k;inp>>k;
        outp<<"Case #"<<test<<": "<<s[k]<<"\n";

    }
}
