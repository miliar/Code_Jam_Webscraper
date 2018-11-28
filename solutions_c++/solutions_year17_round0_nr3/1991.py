#include <bits/stdc++.h>
using namespace std;
struct _ { ios_base::Init i; _() { cin.sync_with_stdio(0); cin.tie(0);cout.tie(0); } } _;
#define READ(FILE) freopen(FILE,"r",stdin)
#define WRITE(FILE) freopen(FILE,"w",stdout)
#define ict int t;cin>>t;while(t--)
#define lct long long int t;cin>>t;while(t--)
#define in(a) int a; cin>>a;
#define llin(a) ll a; cin>>a;
#define srep(i,a,b) for(ll i=a;i<b;i++)
#define rep(i,n) for(ll i=0;i<n;i++)
#define pb push_back
typedef long long int ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef pair<ll,ll> pll;
typedef set<int> si;
typedef set<ll> sl;
typedef map<string, ll> mapsl;
typedef map<string, int> mapsi;
typedef map<int,int> mapii;
typedef map<ll, ll> mapll;

pll calc(ll n,ll k)
{
    if(n==k)
        return make_pair(0,0);
    if(k==0 || n==0)
        return make_pair(-1,-1);
    if(n==1)
        return make_pair(0,0);

    if(k==1)
    {
        if(n%2==0)
            return make_pair(n/2 -1,n/2);
        else
            return make_pair(n/2,n/2);
    }

    if(k%2==0)
        return calc(n/2,k/2);
    else
        if(n%2!=0)
            return calc(n/2,(k-1)/2);
        else
            return calc(n/2 -1,k/2);
}

int main()
{
    freopen("inputFiles/C-large.in","r",stdin);
    freopen("inputFiles/ans.txt","w",stdout);
    llin(T);
    for(ll t=1;t<=T;t++)
    {
        llin(n);
        llin(k);
        pll pr=calc(n,k);
        ll LS=pr.first;
        ll RS=pr.second;
        cout<<"Case #"<<t<<": "<<max(LS,RS)<<" "<<min(LS,RS)<<endl;
    }

}
