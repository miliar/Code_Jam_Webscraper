
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


int check(ll n)
{
    vi v;
    while(n)
    {
        v.pb(n%10);
        n/=10;
    }

    int f = 1;

    if(sz(v)>1)
    {
        for(int j=1;j<sz(v);j++)
        {
            if(v[j]>v[j-1])
                f=0;
        }
    }
    return f;
}

int rpos(ll n)
{
    vi v;
    while(n)
    {
        v.pb(n%10);
        n/=10;
    }

    for(int i=sz(v)-2;i>=0;i--)
        if(v[i]<v[i+1])
            return (sz(v)-i-1);
}

string solve(ll x, int pos)
{

    ll f=0,i;
    ll xx=x;
    string sp=tostring(x);
    if(sp[0]=='1')
    {
        f=1;
        for(i=1;i<sz(sp);i++)
            if(sp[i]!='0')
                f=0;
        if(x>1)
        {
            {
                x--;
                sp = tostring(x);
            }
        }
    }

    if(f==1)
        return sp;
    x=xx;
    sp=tostring(x);
    if(check(x))
    {
        for(i=pos-1;i>=0;i--)
        {
            sp[i]=(x%10)+48;
            x/=10;
        }
        return sp;
    }
    x=xx;
    sp=tostring(x);

    int pos1 = rpos(x);

    string s = solve(toint(sp.substr(0,pos1))-1, pos1);

    string s1(sz(sp)-pos1,' ');
    for(i=0;i<sz(sp)-pos1;i++)
        s1[i]='9';
    s+=s1;
    return s;
}

int main()
{

    fr;
    frc;

    ios_base::sync_with_stdio(false); cin.tie(0);
    ll i,j,n,tt,cs=1;

    string st;
    cin>>tt;
    while(tt--)
    {
        cin>>n;
        st = tostring (n);
        string ans = solve(n,sz(st));

        i=0;
        while(i<sz(ans))
        {
            if(ans[i]=='0')
                i++;
            else
                break;
        }

        ans=ans.substr(i,sz(ans)-i);
        cout<<"Case #"<<cs<<": ";
        cout<<ans<<endl;
        cs++;
    }


    return 0;
}
