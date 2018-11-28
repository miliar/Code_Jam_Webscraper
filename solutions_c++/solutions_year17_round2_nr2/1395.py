
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
#define fr freopen("x2.in","r",stdin)
#define frc freopen("y2.txt","w",stdout)
#define all(x) x.begin(),x.end()
#define set0(x) memset(x,0,sizeof(x))
#define dbg cout<<"yo "<<endl;

#define pii pair<int,int>
#define pll pair<ll,ll>
#define vpii vector<pair<int,int> >
#define si set<int>
#define mii map<int,int>
#define umii unordered_map<int,int>
#define vi vector<int>
#define pb push_back
#define ff first
#define ss second
#define mp make_pair

typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> OST;

ll toint(const string &s) { stringstream ss; ss << s; ll x; ss >> x; return x; }
string tostring ( ll number ){  stringstream ss; ss<< number; return ss.str();}

const lf pi = 2*acos(0);
const int nn = 2123456;

ll gcd(ll a,ll b){return (b==0)? a:gcd(b,a%b); }
void nope(int num = 0){ if(num==0) cout<<"NO"; else cout<<"-1"; exit(0); }

char a[4000];
void solve(int x)
{
    ll i,j,n;
    cin>>n;
    int r,y,o,g,b,v;
    cin>>r>>o>>y>>g>>b>>v;
    int v1,v2,v3;
    char c1,c2,c3;
    for(i=0;i<=3030;i++)
        a[i]='X';
    if(r>=y and r>=b )
    {
        v1=r;
        c1 = 'R';
        if(y>=b )
        {
            v2 = y;
            c2='Y';
            v3 = b;
            c3= 'B';
        }
        else
        {
            v2 = b;
            c2='B';
            v3 = y;
            c3= 'Y';
        }
    }

    else if(y>=r and y>=b )
    {
        v1=y;
        c1 = 'Y';
        if(r>=b )
        {
            v2 = r;
            c2 = 'R';
            v3 = b;
            c3 = 'B';
        }
        else
        {
            v2 = b;
            c2 = 'B';
            v3 = r;
            c3 = 'R';
        }
    }

    else if(b>=y and b>=r )
    {
        v1=b;
        c1 = 'B';
        if(y>=r )
        {
            v2 = y;
            c2 = 'Y';
            v3 = r;
            c3 = 'R';
        }
        else
        {
            v2 = r;
            c2 = 'R';
            v3 = y;
            c3 = 'Y';
        }
    }

    i=0;
    rep(j,v1)
    {
        a[i]=c1;
        i+=3;
    }

    i=1;
    rep(j,v2)
    {
        a[i]=c2;
        i+=3;
    }

    i=3*(v1-1)+2;
    rep(j,v3)
    {
        a[i]=c3;
        i-=3;
    }

    vector<char>ve;
    for(i=0;i<=3030;i++)
        if(a[i]!='X')
            ve.pb(a[i]);

    int p = sz(ve),f=0;
    for(i=0;i<sz(ve);i++)
    {
        if(ve[i]==ve[(i+1)%p])
        {
            f=-1;
        }
    }

    cout<<"Case #"<<x<<": ";
    if(f==-1)
        cout<<"IMPOSSIBLE"<<endl;
    else
    {
        for(i=0;i<p;i++)
        {
            cout<<ve[i];
        }
        cout<<endl;
    }
}

int main()
{

    ios_base::sync_with_stdio(false); cin.tie(0);

    fr;
    frc;

    ll i,j,n,tt;
    tt=1;
    cin>>tt;
    int x = 1;
    while(tt--)
    {
        solve(x);
        x++;
    }
    return 0;
}

