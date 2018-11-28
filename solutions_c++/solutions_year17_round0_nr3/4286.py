

#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace __gnu_pbds;
using namespace std;

#define inf 1013161010
#define ninf -1013161010
#define mod 1000000007
#define ll long long
#define lf long double
#define in(x) scanf("%d",&x);
#define sz(x) ((int)x.size())
#define lld l64d
#define rep(i,n) for(i=0;i<n;i++)
#define rrep(i,n) for(i=n-1;i>=0;i--)
#define rep1(i,a,b) for(i=a;i<=b;i++)
#define rrep1(i,a,b) for(i=a;i>=b;i--)
#define stlfor(i,t) for(auto i =t.begin();i!=t.end();i++)
#define fr freopen("x.in","r",stdin)
#define frc freopen("y.txt","w",stdout)
#define all(x) x.begin(),x.end()
#define set0(x) memset(x,0,sizeof(x))
#define dbg cout<<"yo "<<endl;

#define pii pair<int,int>
#define pll pair<ll,ll>
#define mii map<int,int>
#define umii unordered_map<int,int>
#define vi vector<int>
#define pb push_back
#define ff first
#define ss second
#define mp make_pair

typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> OST;

int toint(const string &s) { stringstream ss; ss << s; int x; ss >> x; return x; }
string tostring ( int number ){  stringstream ss; ss<< number; return ss.str();}

const lf pi = 2*acos(0);
const int nn = 2123456;

ll gcd(ll a,ll b){return (b==0)? a:gcd(b,a%b); }

vector<pair<int,int> > v;
void solve(ll x,ll y)
{
    if(y-x<=1)
        return;
    ll mid = (x+y)/2;
    ll sze = (y-x)/2;
    if((x+y)%2==0)
        v.pb(mp(sze-1,sze-1));
    else
        v.pb(mp(sze,sze-1));
    solve(x,mid);
    solve(mid,y);
}

int main()
{
    fr;
    frc;

    ios_base::sync_with_stdio(false); cin.tie(0);
    ll i,j,k,n,tt,cs=1;
    cin>>tt;
    while(tt--)
    {
        v.clear();
        cin>>n>>k;
        solve(0,n+1);
        sort(all(v),greater<pair<int,int> >());
        cout<<"Case #"<<cs<<": ";
        cout<<v[k-1].ff<<" "<<v[k-1].ss<<endl;
        cs++;
    }

    return 0;
}

